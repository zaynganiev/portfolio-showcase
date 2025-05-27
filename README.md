# Portfolio Showcase

A web application created by Zayn Ganiev to showcase portfolio projects and allow anyone to contact me directly via email.

## Features

- **Portfolio Display:** Presenting projects and skills in a clean, interactive format.
- **Contact Form:** Visitors can send me messages directly from the site.
- **Email Integration:** Uses a secure SMTP connection to send emails from the contact form.
- **Environment Variables:** Sensitive information (like email credentials) is managed securely using a `.env` file.

## Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) for the web interface
- [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variable management
- [smtplib](https://docs.python.org/3/library/smtplib.html) and [ssl](https://docs.python.org/3/library/ssl.html) for sending emails

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/portfolio-showcase.git
   cd portfolio-showcase
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file:**
   ```
   EMAIL_USERNAME="your_email@gmail.com"
   EMAIL_PASSWORD="your_app_password"
   EMAIL_RECEIVER="your_email@gmail.com"
   ```

4. **Run the app:**
   ```sh
   streamlit run pages/Contact_Us.py
   ```

## Usage

- Open the app in your browser.
- Fill out the contact form to send a message.
- Feel free to deploy.

## Security

- Never commit your `.env` file or sensitive credentials to version control.
- Use app-specific passwords for email services when possible.

## License

This project is licensed under the MIT License.
