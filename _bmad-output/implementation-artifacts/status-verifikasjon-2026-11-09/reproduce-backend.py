import json
import tempfile
from datetime import datetime
from pathlib import Path
from fastapi.testclient import TestClient
from vaktmatch.config import DEFAULT_DATA_DIR, Settings
from vaktmatch.data import DatasetRepository
from vaktmatch.data.schema import Absence, Dataset
from vaktmatch.main import create_app
from vaktmatch.rules.engine import evaluate

original = DatasetRepository(DEFAULT_DATA_DIR).get_dataset('hovedscenario')
raw = original.model_dump(mode='json')
shift = next(s for s in raw['shifts'] if s['id'] == 'W5-A02-1')
shift['end'] = datetime.fromisoformat(shift['end']).replace(hour=23).isoformat()
modified = Dataset.model_validate(raw)
result = evaluate(modified, [Absence(employee_id='A01', shift_id='X')], 'X', 0, ['P1'])
a02 = next(a for a in result['alternatives'] if a['candidate_id'] == 'A02')
person = a02['consequences'][0]
r4 = next(r for r in person['rules'] if r['rule'] == 'R4')
out = [{'finding':'r4_hidden_interval', 'status':str(r4['status']), 'value':r4['value'], 'rest_after':person['rest_after']}]

with tempfile.TemporaryDirectory(prefix='vaktmatch-family-') as folder:
    for identifier in ('family-a','family-b'):
        source = original.model_dump(mode='json')
        source['dataset']['id'] = identifier
        source['dataset'].pop('family_id')
        Path(folder, identifier+'.json').write_text(json.dumps(source),encoding='utf-8')
    client = TestClient(create_app(Settings(data_dir=Path(folder),_env_file=None)))
    response = client.post('/api/datasets/compare',json={'previous_id':'family-a','next_id':'family-b'})
    out.append({'finding':'empty_family', 'http_status':response.status_code, 'same_family':response.json()['same_family'], 'ids':['family-a','family-b']})

(Path(tempfile.mkdtemp(prefix='vaktmatch-backend-repro-'))/'backend-reproductions.json').write_text(json.dumps(out,default=str,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,default=str))
