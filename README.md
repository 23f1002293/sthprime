# P-th Prime Finder

## Summary

This is a minimal, full-stack application designed to find the p-th prime number. It consists of two main components:
1.  A Python script (`main.py`) that can be run from the command line.
2.  An interactive web interface (`index.html`) that uses JavaScript to perform the same calculation directly in the browser.

## Setup

### Prerequisites

*   **For Command-Line Usage:** Python 3.6 or higher.
*   **For Web Interface:** A modern web browser (e.g., Chrome, Firefox, Safari).

### Installation

No special installation is required.

1.  Clone this repository or download the files.
2.  All necessary code is self-contained within the provided files.

## Usage

### Command-Line Interface

You can run the Python script from your terminal to find the p-th prime.

1.  Navigate to the directory containing the files.
2.  Run the script with the desired position `p` as an argument:

    ```bash
    python main.py <p>
    ```

**Example:**

```bash
$ python main.py 10
The 10-th prime is: 29

$ python main.py 10001
The 10001-th prime is: 104743
```

### Web Interface

The `index.html` file provides a user-friendly way to find primes.

1.  Open the `index.html` file in your web browser.
2.  Enter a positive integer into the input field.
3.  Click the "Find Prime" button.
4.  The result will be displayed on the page below the button.

## Code Explanation

### `main.py`

This script contains the core logic for finding prime numbers, written in Python.

*   `is_prime(n)`: A function that checks if a given number `n` is prime. It uses an optimized trial division method that skips multiples of 2 and 3.
*   `get_pth_prime(p)`: This function iterates through odd numbers, using `is_prime()` to identify primes. It keeps a count until it finds the p-th prime and returns it.
*   `if __name__ == "__main__":`: The main execution block parses command-line arguments, calls the prime-finding logic, handles potential errors (like non-integer input), and prints the result to the console.

### `index.html`

This file is a self-contained HTML document with embedded CSS and JavaScript for the interactive frontend.

*   **HTML**: Defines the structure of the page, including a title, a form with a number input field, and a submit button. A `div` with the id `result` is used as a placeholder for the output.
*   **CSS**: A small `<style>` block provides basic styling to center the content and make the interface look clean and usable.
*   **JavaScript**: The `<script>` block contains the client-side logic.
    *   It includes JavaScript implementations of `isPrime()` and `getPthPrime()`, which mirror the logic from the Python script.
    *   An event listener is attached to the form's `submit` event.
    *   When the form is submitted, it prevents the default page reload, reads the input value, calls the `getPthPrime()` function, and displays the formatted result in the `result` div.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
