# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright==1.58.0"]
# ///
import json
import tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

output = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    preview_calls = []
    def preview(route):
        preview_calls.append(route.request.post_data_json)
        route.abort() if len(preview_calls) == 1 else route.continue_()
    page.route('**/api/absences/preview', preview)
    page.goto('http://127.0.0.1:5173/')
    page.get_by_role('button', name='Registrer fravær', exact=True).click()
    expect(page.get_by_text('Backend er utilgjengelig.', exact=False)).to_be_visible()
    page.get_by_role('button', name='Simuler fravær', exact=True).click()
    page.get_by_role('button', name='Prøv igjen', exact=True).click()
    output.append({'finding':'preview_retry', 'preview_requests_after_retry':len(preview_calls), 'target_choices_after_retry':page.get_by_role('radio').count(), 'form_error_visible':page.get_by_text('Velg ett framtidig målskift i uke 5.', exact=True).count() > 0})
    page.locator('#days').fill('2')
    page.get_by_role('radio').first.wait_for()
    output[-1]['preview_requests_after_field_change'] = len(preview_calls)
    output[-1]['target_choices_after_field_change'] = page.get_by_role('radio').count()
    page.unroute('**/api/absences/preview')
    page.goto('http://127.0.0.1:5173/')
    page.get_by_role('button', name='Datagrunnlag', exact=True).click()
    page.locator('#dataset').select_option('en-flytting')
    page.get_by_role('button', name='Forhåndsvis endringer', exact=True).click()
    page.get_by_role('button', name='Last inn oppdaterte vaktdata', exact=True).click()
    expect(page.get_by_role('heading', name='Ukesoversikt', exact=True)).to_be_visible()
    page.get_by_role('button', name='Datagrunnlag', exact=True).click()
    value = page.locator('#dataset').input_value()
    enabled = page.get_by_role('button', name='Forhåndsvis endringer', exact=True).is_enabled()
    with page.expect_request('**/api/datasets/compare') as pending:
        page.get_by_role('button', name='Forhåndsvis endringer', exact=True).click()
    output.append({'finding':'dataset_selection', 'displayed_value':value, 'preview_enabled':enabled, 'comparison_body':pending.value.post_data_json})
    page.goto('http://127.0.0.1:5173/')
    page.get_by_role('button', name='Registrer fravær', exact=True).click()
    page.get_by_role('radio').first.wait_for()
    page.get_by_role('button', name='Simuler fravær', exact=True).click()
    page.locator('#search-limit').select_option('0')
    with page.expect_response('**/api/evaluate') as response:
        page.get_by_role('button', name='Finn alternativer', exact=True).click()
    result = response.value.json()
    a05 = next(a for a in result['alternatives'] if a['candidate_id'] == 'A05')
    page.get_by_text('Øvrige undersøkbare funn', exact=False).click()
    page.locator('#inspect-' + a05['id']).click()
    page.get_by_role('button', name='Tilbake til alternativer', exact=True).click()
    details = page.locator('details').filter(has=page.get_by_text('Øvrige undersøkbare funn', exact=False))
    page.wait_for_function("document.querySelector('h1')?.textContent === 'Sammenlign alternativer'")
    output.append({'finding':'back_to_list', 'other_findings_open':details.evaluate('(element) => element.open'), 'focus_on_origin_button':page.evaluate('(id) => document.activeElement?.id === id', 'inspect-' + a05['id']), 'origin_button_visible':page.locator('#inspect-' + a05['id']).is_visible()})
    page.locator('#search-limit').select_option('1')
    with page.expect_response('**/api/evaluate') as response:
        page.get_by_role('button', name='Finn alternativer', exact=True).click()
    result = response.value.json()
    matches = [a for a in result['alternatives'] if a['candidate_id'] == 'A08' and a['selectable'] and a['affected_employee_ids'] == ['A06','A08']]
    chosen = [next(a for a in matches if 'W5-A08-4' in a['affected_shift_ids']), next(a for a in matches if 'W5-A08-5' in a['affected_shift_ids'])]
    for a in chosen:
        page.get_by_role('button', name='2 Alternativer', exact=True).click()
        page.locator('#inspect-' + a['id']).click()
        page.get_by_role('button', name='Velg alternativ', exact=True).click()
    page.get_by_role('button', name='2 Alternativer', exact=True).click()
    direct = next(a for a in result['alternatives'] if a['candidate_id'] == 'A02' and a['moves'] == 0 and a['selectable'])
    page.locator('#inspect-' + direct['id']).click()
    page.get_by_role('button', name='Velg alternativ', exact=True).click()
    page.get_by_text('Tidligere valg (2)', exact=True).click()
    history_texts = page.locator('details article').all_inner_texts()
    output.append({'finding':'ambiguous_history', 'distinct_proposal_ids':[a['id'] for a in chosen], 'distinct_shift_sets':[a['affected_shift_ids'] for a in chosen], 'history_records':len(history_texts), 'identical_history_text':len(history_texts)==2 and history_texts[0]==history_texts[1]})
    browser.close()
(Path(tempfile.mkdtemp(prefix='vaktmatch-ui-repro-'))/'ui-reproductions.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(output,ensure_ascii=True))
