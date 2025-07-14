describe('MTN App Launch Flow', function () {
    it('should launch app and verify number', function () {
        browser.setTimeout({ implicit: 30000 });

        // Click permission allow button
        const firstAction = $('id=com.android.permissioncontroller:id/permission_allow_button');
        firstAction.click();

        // Click get started button
        const secondAction = $('//android.view.ViewGroup[@content-desc="get_started_btn"]/android.view.ViewGroup');
        secondAction.click();

        // Input phone number
        const inputField = $('//android.widget.EditText[@content-desc="login_input_msisdn"]');
        inputField.setValue('0593130530');

        // Click checkbox
        const checkbox = $('android.widget.CheckBox');
        checkbox.click();

        // Click verify number button
        const verifyBtn = $('//android.view.ViewGroup[@content-desc="login_btn_verify_number"]/android.view.ViewGroup');
        verifyBtn.click();
    });
});
