from demo_automated_testing import translate_dna
import pytest

def test_a_to_t():
    assert translate_dna("A") == "T"

def test_t_to_a():
    assert translate_dna("T") == "A"

def test_c_to_g():
    assert translate_dna("C") == "G"

def test_g_to_c():
    assert translate_dna("G") == "C"

def test_non_protein():
    assert translate_dna("Z") == "not valid"
