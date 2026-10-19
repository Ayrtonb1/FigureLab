from pathlib import Path

from figurelab.projects.models import Measurement, Project


def test_project_can_group_measurements():
    measurement = Measurement(
        technique="xrd",
        source_path=Path("sample_data/xrd/example.xy"),
        sample_id="sample-001",
    )
    project = Project(name="demo", measurements=(measurement,))

    assert project.measurements[0].sample_id == "sample-001"
