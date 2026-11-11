import inspect
import json
import sys
from pathlib import Path
import pytest
import vaktmatch.api.routes as routes
import vaktmatch.rules.engine as engine

mode=sys.argv[1]
if mode == 'readable-diff':
    original=routes.readable_change
    routes.readable_change=lambda change:{**original(change),'label':'','before_label':'','after_label':''}
elif mode == 'secondary-criterion':
    source=inspect.getsource(engine.rank_alternatives)
    assert 'for c in criteria)' in source
    exec(source.replace('for c in criteria)','for c in criteria[:1])'),engine.__dict__)
else:
    raise ValueError(mode)
code=pytest.main(['-q',str(Path(__file__).resolve().parents[3]/'backend/tests')])
print(json.dumps({'mutation':mode,'pytest_exit_code':code,'scope':'Process-local only; repository files unchanged'}))
raise SystemExit(code)
