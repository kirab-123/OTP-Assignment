from unittest.mock import patch
from Otp_Version_2 import (
    validateMobile,
    validateEmailID,
    generateOtp,
    sendOTPOverMobile,
    sendOTPOverEmail,
)

# Define your test cases
def test_validateMobile():
    assert validateMobile("1234567890") is True
    assert validateMobile("12345") is False
    assert validateMobile("abcdefghij") is False

def test_validateEmailID():
    assert validateEmailID("user@example.com") is True
    assert validateEmailID("invalid-email") is False
    assert validateEmailID("user@example") is False

def test_generateOtp():
    otp = generateOtp(6)
    assert len(otp) == 6
    assert otp.isdigit()

@patch("your_script_file.smtplib.SMTP")
def test_sendOTPOverEmail(mock_smtp):
    receiver = "user@example.com"
    otp = "123456"
    sendOTPOverEmail(receiver, otp)
    mock_smtp.assert_called_with("smtp.gmail.com", 587)

@patch("your_script_file.twilio.rest.Client.messages.create")
def test_sendOTPOverMobile(mock_twilio_create):
    target = "1234567890"
    otp = "123456"
    sendOTPOverMobile(target, otp)
    mock_twilio_create.assert_called_with(
        body="Your OTP is 123456. Valid for next 15 minutes.",
        from_="+12697679255",
        to="+911234567890",
    )

# Run the tests with pytest
if __name__ == "__main__":
    import pytest

    pytest.main()