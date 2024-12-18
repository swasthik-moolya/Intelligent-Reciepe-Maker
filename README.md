# Intelligent Recipe Maker (IRM)

**Table of Contents**

*   [Project Overview](#project-overview)
*   [Installation](#installation)
*   [Usage](#usage)
    *   [Ingredient-Based Recommendations](#ingredient-based-recommendations)
    *   [Dietary Restriction Support](#dietary-restriction-support)
*   [Contributing](#contributing)
*   [License](#license)

## Project Overview

IRM is a Python application that facilitates intelligent recipe creation and recommendation. It offers various functionalities to personalize your culinary exploration.

## Installation

1.  **Prerequisites:**

    *   Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
    *   Necessary libraries (install using `pip install`):
        *   `pandas` (data manipulation)
        *   `nltk` (Natural Language Toolkit for text processing)
        *   [Optional] Web scraping library (e.g., `beautifulsoup4` or `requests`) for recipe dataset creation (discussed later)

2.  **Clone the repository:**

    ```bash
    git clone [https://github.com/swasthik-moolya/Intelligent-Recipe-Maker.git](https://github.com/swasthik-moolya/Intelligent-Recipe-Maker.git)
    cd Intelligent-Recipe-Maker
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**

    ```bash
    python main.py
    ```

2.  **Ingredient-Based Recommendations:**

    *   Enter a comma-separated list of ingredients you have on hand.

    ```
    Enter ingredients (comma-separated): onion, bell pepper, chicken breast
    ```

    *   IRM will suggest recipes that utilize these ingredients.

3.  **Dietary Restriction Support:**

    *   Specify your dietary preferences:

        *   `vegetarian`
        *   `vegan`
        *   `gluten-free`
        *   [Custom dietary restrictions]

    ```
    Enter dietary restrictions (if none, leave blank): vegetarian
    ```

    *   IRM will tailor recommendations to match your restrictions.

## Contributing

We welcome contributions to improve IRM! Please feel free to submit pull requests or report issues on GitHub.

## License

This project is licensed under the MIT License (see LICENSE file) for open-source collaboration.
