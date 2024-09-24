from isp_trace_parser import directory_structure_formatter


def test_write_solar_save_names():
    meta_data = {
        "name": "a",
        "year": "1",
        "technology": "x",
        "file_type": "project",
        "hy": "2",
    }

    save_filepath = directory_structure_formatter.write_new_solar_filepath(meta_data)

    assert str(save_filepath) == "RefYear1/Project/a/RefYear1_a_x_HalfYear2.parquet"

    meta_data = {
        "name": "a",
        "year": "1",
        "technology": "x",
        "file_type": "area",
        "hy": "2",
    }

    save_filepath = directory_structure_formatter.write_new_solar_filepath(meta_data)

    assert str(save_filepath) == "RefYear1/Area/a/x/RefYear1_a_x_HalfYear2.parquet"


def test_write_wind_save_names():
    meta_data = {"name": "a", "year": "1", "file_type": "project", "hy": "2"}

    save_filepath = directory_structure_formatter.write_new_wind_filepath(meta_data)

    assert str(save_filepath) == "RefYear1/Project/a/RefYear1_a_HalfYear2.parquet"

    meta_data = {
        "name": "a",
        "year": "1",
        "resource_type": "x",
        "file_type": "area",
        "hy": "2",
    }

    save_filepath = directory_structure_formatter.write_new_wind_filepath(meta_data)

    assert str(save_filepath) == "RefYear1/Area/a/x/RefYear1_a_x_HalfYear2.parquet"


def test_write_demand_save_names():
    meta_data = {
        "scenario": "a",
        "year": "1",
        "area": "x",
        "poe": "poe10",
        "descriptor": "y",
        "hy": "2",
    }

    save_filepath = directory_structure_formatter.write_new_demand_filepath(meta_data)

    assert (
        str(save_filepath)
        == "a/RefYear1/x/poe10/y/a_RefYear1_x_poe10_y_HalfYear2.parquet"
    )
