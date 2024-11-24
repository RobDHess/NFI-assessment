from .utils import create_inputs, run_script


def test_simple():
    """Test the script with a simple input"""
    inputs = create_inputs(["WTG", "ATG"])
    result = run_script(inputs)
    assert "Het DNA profiel past in spoor" in result.stdout


def test_multiple_profiels():
    """Test the script with multiple DNA profiels for a single spoor"""
    spoor = "ATG"
    profiels = ["ATT", "ATC", "ATG"]
    inputs = create_inputs([spoor] + profiels)
    result = run_script(inputs)
    assert "Het DNA profiel past in spoor" in result.stdout
    assert "Het DNA profiel past niet in spoor" in result.stdout


def test_length_mismatch():
    """Test for mismatched lengths of DNA spoor and profiel"""
    spoor = "ATG"
    profiel = "AT"
    inputs = create_inputs([spoor, profiel])
    result = run_script(inputs)
    assert "Het DNA profiel past niet in spoor" in result.stdout

    spoor = "AT"
    profiel = "ATG"
    inputs = create_inputs([spoor, profiel])
    result = run_script(inputs)
    assert "Het DNA profiel past niet in spoor" in result.stdout


def test_all_iupac():
    """Test all possible IUPAC matches with a comprehensive spoor"""
    spoor = "ATCGWWSSMMKKRRYYBBBDDDHHHVVVNNNN"
    profiel = "ATCGATCGACGTAGCTCGTAGTACTACGACGT"

    inputs = create_inputs([spoor, profiel])
    result = run_script(inputs)
    assert "Het DNA profiel past in spoor" in result.stdout


def test_exact_match():
    """Test for an exact match between spoor and profiel"""
    spoor = "ATG"
    profiel = "ATG"
    inputs = create_inputs([spoor, profiel])
    result = run_script(inputs)
    assert "Het DNA profiel past in spoor" in result.stdout


def test_no_valid_matches():
    """Test the script with profiels that do not match the spoor"""
    spoor = "ATG"
    profiels = ["TTT", "ACC"]
    inputs = create_inputs([spoor] + profiels)
    result = run_script(inputs)
    assert "Het DNA profiel past niet in spoor" in result.stdout


def test_case_insensitivity():
    """Test the script with lowercase and mixed case inputs"""
    spoor = "atg"
    profiel = "ATG"
    inputs = create_inputs([spoor, profiel])
    result = run_script(inputs)
    assert "Het DNA profiel past in spoor" in result.stdout


def test_new_spoor():
    """Test entering a new spoor after processing one"""
    spoor1 = "ATG"
    profiel1 = "ATG"
    spoor2 = "ACG"
    profiel2 = "ACG"
    inputs = create_inputs([spoor1, profiel1, "SPOOR", spoor2, profiel2])
    result = run_script(inputs)
    assert "Het DNA profiel past in spoor" in result.stdout
