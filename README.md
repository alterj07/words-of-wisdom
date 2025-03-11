# raspAPI

A motivational quote generator API built with Python Flask for Hack Club's Raspberry API YSWS.

## Overview

raspAPI is a quote generator that provides inspirational content whenever you need a boost. This project is my first experience working with Python Flask and creating an API.

## Features

- **Quote Generation**: Get random motivational quotes to inspire you
- **Custom Quotes**: Add your own motivational quotes to the database
- **User Authentication**: Secure access with username/password login

## Getting Started

### Prerequisites

- Python 3.6+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/alterj07/words-of-wisdom.git
   cd words-of-wisdom
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```


### Authentication

To use raspAPI, you need to create an account or use the default credentials:

- Username: `user`
- Password: `pass`

### API Endpoints

- `GET /quotes` - Retrieve a random quote
- `POST /quotes` - Add a new quote (requires authentication)
- `GET /quotes/all` - Retrieve all quotes (requires authentication)


