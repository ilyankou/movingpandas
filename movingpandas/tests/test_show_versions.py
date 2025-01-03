# -*- coding: utf-8 -*-

from movingpandas.tools._show_versions import (
    _get_C_info,
    _get_deps_info,
    _get_sys_info,
    show_versions,
)


def test_get_sys_info():
    sys_info = _get_sys_info()

    assert "python" in sys_info
    assert "executable" in sys_info
    assert "machine" in sys_info


def test_get_c_info():
    C_info = _get_C_info()

    assert "PROJ" in C_info
    assert "PROJ data dir" in C_info


def test_get_deps_info():
    deps_info = _get_deps_info()

    assert "geopandas" in deps_info
    assert "pandas" in deps_info
    assert "pyproj" in deps_info
    assert "numpy" in deps_info
    assert "shapely" in deps_info
    assert "pyproj" in deps_info
    assert "matplotlib" in deps_info
    assert "mapclassify" in deps_info
    assert "geopy" in deps_info
    assert "holoviews" in deps_info
    assert "hvplot" in deps_info
    assert "geoviews" in deps_info


def test_show_versions(capsys):
    show_versions()
    out, err = capsys.readouterr()

    assert "python" in out
    assert "PROJ" in out
    assert "geopandas" in out
