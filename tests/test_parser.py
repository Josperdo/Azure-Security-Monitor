from pathlib import Path
from src.parser import load_activity_logs

def test_load_activity_logs_parses_sample():
    p = Path(__file__).resolve().parents[1] / "data" / "sample_activity_logs.json"
    events = load_activity_logs(str(p))
    assert isinstance(events, list)
    assert len(events) >= 1