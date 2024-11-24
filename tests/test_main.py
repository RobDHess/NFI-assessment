from .utils import create_inputs, run_script


def test_exit():
    """Test whether the script exits successfully"""
    inputs = create_inputs([])
    result = run_script(inputs)
    assert result.returncode == 0, f"Script exited with error: {result.stderr}"


def test_invalid_input():
    """Test the script with invalid input, both as spoor input and as profiel"""
    # Check spoor input
    illegal_inputs = ["Meow", "124", "#$%", "ATCGTX"]
    for illegal_input in illegal_inputs:
        inputs = create_inputs([illegal_input])
        result = run_script(inputs)
        assert "Een DNASpoor mag alleen bestaan uit" in result.stdout

    # Check DNA profiel input
    valid_input = "ATCGWSMKRYBDHVN"
    for illegal_input in illegal_inputs:
        inputs = create_inputs([valid_input, illegal_input])
        result = run_script(inputs)
        assert "Het DNA profiel past" not in result.stdout


def test_early_exit():
    """Test exiting the script after entering a spoor"""
    spoor = "ATTCGWTTBATTVGCT"
    inputs = create_inputs([spoor], close=True)
    result = run_script(inputs)
    assert result.returncode == 0


def test_special_commands_in_inputs():
    """Test for 'X' or 'SPOOR' within the spoor or profile"""
    spoor = "ATTCGWXTTATTVGCT"
    inputs = create_inputs([spoor])
    result = run_script(inputs)
    assert "Een DNASpoor mag alleen bestaan uit" in result.stdout
