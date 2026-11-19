from utils.response_parser import extract_sections


def test_extracts_both_sections():
    response = (
        "**Possible Causes**\nA few general possibilities.\n\n"
        "**Home Remedies**\n- Rest\n- Drink fluids"
    )

    result = extract_sections(response)

    assert result["possible_causes"] == "A few general possibilities."
    assert "- Rest" in result["home_remedies"]


def test_missing_sections_returns_empty_strings():
    result = extract_sections("A response without section headings.")

    assert result == {"possible_causes": "", "home_remedies": ""}



def test_extracts_multiple_remedy_bullet_points():
    response = (
        "**Possible Causes**\nDehydration.\n\n"
        "**Home Remedies**\n- Drink water\n- Rest\n- Sleep"
    )

    result = extract_sections(response)

    assert "- Drink water" in result["home_remedies"]
    assert "- Rest" in result["home_remedies"]
    assert "- Sleep" in result["home_remedies"]


def test_handles_empty_response():
    result = extract_sections("")

    assert result == {
        "possible_causes": "",
        "home_remedies": ""
    }


def test_handles_only_one_section():
    response = "**Possible Causes**\nLack of sleep."

    result = extract_sections(response)

    assert result["possible_causes"] == "Lack of sleep."
    assert result["home_remedies"] == ""
