import pytest
from unittest.mock import patch
from extract_data import (
    create_string_replacements,
    extract_villain,
    which_standard,
    extract_difficulty,
    clean_up_hero_name,
    clean_up_aspect
)

# Mock config data for testing
MOCK_VILLAIN_CONFIG = {
    "Ultron": {"replacements": ["ultron", "ULTRON", "ultron drone"]},
    "Kang": {"replacements": ["kang", "KANG"]},
    "Rhino": {"replacements": [None]}
}

MOCK_HERO_CONFIG = {
    "Thor": {"replacements": ["thor", "THOR", "god of thunder"]},
    "Iron Man": {"replacements": ["iron man", "IRON MAN", "tony stark"]},
    "Spider-Man": {"replacements": ["spider-man", "SPIDER-MAN", "spidey"]}
}


def test_create_string_replacements():
    # Test with mock villain config
    result = create_string_replacements(MOCK_VILLAIN_CONFIG)
    assert result["ultron"] == "Ultron"
    assert result["ultron drone"] == "Ultron"
    assert result["kang"] == "Kang"
    assert result["rhino"] == "Rhino"
    # Test with None replacements
    assert len([k for k, v in result.items() if v == "Rhino"]) == 1

    # Edge case: empty config
    assert create_string_replacements({}) == {}

@patch('extract_data.villain_config_data', MOCK_VILLAIN_CONFIG)
def test_extract_villain():
    # Normal cases
    assert extract_villain("Defeated Ultron today") == "Ultron"
    assert extract_villain("KANG was tough") == "Kang"
    assert extract_villain("Rhino charged ahead") == "Rhino"
    # Case insensitivity
    assert extract_villain("ultron DRONE appeared") == "Ultron"
    # No match
    assert extract_villain("No villain here") == "UNKNOWN"
    # Empty string
    assert extract_villain("") == "UNKNOWN"
    # Multiple matches (should return first match)
    assert extract_villain("Ultron and Kang fought") == "Ultron"

def test_which_standard():
    # Normal cases
    assert which_standard("Standard 2 rules") == "S2"
    assert which_standard("Played Standard II") == "S2"
    assert which_standard("Standard 3 mode") == "S3"
    assert which_standard("Standard III here") == "S3"
    assert which_standard("Just standard") == "S1"
    # Case insensitivity
    assert which_standard("STANDARD 2") == "S2"
    # Edge cases
    assert which_standard("") == "S1"
    assert which_standard("No standard mentioned") == "S1"

def test_extract_difficulty():
    # Comprehensive difficulty levels
    assert extract_difficulty("S1E1 Ultron") == "S1E1"
    assert extract_difficulty("S1E2 mode") == "S1E2"
    assert extract_difficulty("S2E1 rules") == "S2E1"
    assert extract_difficulty("S2E2 tough") == "S2E2"
    assert extract_difficulty("S3E1 game") == "S3E1"
    assert extract_difficulty("S3E2 hard") == "S3E2"
    # Standard levels
    assert extract_difficulty("S2 only") == "S2"
    assert extract_difficulty("S3 play") == "S3"
    # Expert levels
    assert extract_difficulty("Expert mode") == "S1E1"
    assert extract_difficulty("Expert 2") == "S1E2"
    assert extract_difficulty("Standard 2 Expert II") == "S2E2"
    # Heroic
    assert extract_difficulty("Heroic challenge") == "Heroic"
    # Default
    assert extract_difficulty("No difficulty") == "S1"
    # Case insensitivity
    assert extract_difficulty("s1e1 lowercase") == "S1E1"
    assert extract_difficulty("s1 expert lowercase") == "S1E1"
    assert extract_difficulty("s1e2 lowercase") == "S1E2"
    assert extract_difficulty("s2e1 lowercase") == "S2E1"
    assert extract_difficulty("s2e2 lowercase") == "S2E2"
    assert extract_difficulty("s3e1 lowercase") == "S3E1"
    assert extract_difficulty("s3e2 lowercase") == "S3E2"
    assert extract_difficulty("s1 lowercase") == "S1"
    assert extract_difficulty("s2 lowercase") == "S2"
    assert extract_difficulty("s3 lowercase") == "S3"
    # Edge cases
    assert extract_difficulty("") == "S1"

@patch('extract_data.hero_config_data', MOCK_HERO_CONFIG)
def test_clean_up_hero_name():
    # Normal cases
    assert clean_up_hero_name("thor") == "Thor"
    assert clean_up_hero_name("god of thunder") == "Thor"
    assert clean_up_hero_name("iron man") == "Iron Man"
    assert clean_up_hero_name("spidey") == "Spider-Man"
    # Unknown hero (returns input)
    assert clean_up_hero_name("unknown hero") == "unknown hero"
    # Edge cases
    assert clean_up_hero_name("") == ""
    assert clean_up_hero_name(" ") == " "

def test_clean_up_aspect():
    # Normal cases
    assert clean_up_aspect("justice") == "Justice"
    assert clean_up_aspect("leadership") == "Leadership"
    assert clean_up_aspect("aggression") == "Aggression"
    assert clean_up_aspect("protection") == "Protection"
    # Typos and aliases
    assert clean_up_aspect("jusitce") == "Justice"
    assert clean_up_aspect("prtoection") == "Protection"
    assert clean_up_aspect("blue") == "Leadership"
    assert clean_up_aspect("red") == "Aggression"
    assert clean_up_aspect("yellow") == "Justice"
    assert clean_up_aspect("green") == "Protection"
    assert clean_up_aspect("gray") == "Basic"
    assert clean_up_aspect("grey") == "Basic"
    # Case insensitivity
    assert clean_up_aspect("JUSTICE") == "Justice"
    assert clean_up_aspect("PROTECTION") == "Protection"
    assert clean_up_aspect("AgGrESsion") == "Aggression"
    assert clean_up_aspect("LEADERSHIP") == "Leadership"
    assert clean_up_aspect("GRAY") == "Basic"
    assert clean_up_aspect("GREY") == "Basic"
    # Edge cases
    assert clean_up_aspect("") == ""
    assert clean_up_aspect("unknown") == "Unknown" 