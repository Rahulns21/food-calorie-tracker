# Food Calorie Tracker App

This is a simple web application built with Django and Bootstrap 5 to help users track their daily calorie intake. The app also utilizes Chart.js to display a donut chart summarizing the distribution of consumed calories.

## Features

- **User Authentication**: Users can sign up, log in, and log out securely.
- **Add Food Items**: Users can add food items along with their respective calorie counts for each meal.
- **View Daily Calorie Intake**: Users can see a summary of their daily calorie intake.
- **Donut Chart**: A graphical representation using Chart.js to visualize the distribution of consumed calories.

## Installation

```bash
# Clone this repository:
git clone https://github.com/Rahulns21/food-calorie-tracker.git

# Navigate to the project directory:
cd food-calorie-tracker

# Install dependencies:
pip install -r requirements.txt

# Apply migrations:
python manage.py migrate

# Run the development server:
python manage.py runserver

10. Visit `http://127.0.0.1:8000/` in your web browser to access the application.
   
11. Visit `http://127.0.0.1:8000/admin` in your web browser to access the admin panel ```

## Usage

1. Create a superuser or log in if you already have one.
2. Once logged in, you can add food items along with their calorie counts in the admin panel.
3. View your daily calorie intake summary.
4. Explore the donut chart to visualize your calorie consumption distribution.

## Dependencies

- Django
- Bootstrap 5
- Chart.js

## Credits

This project was created by [Rahulns21](https://github.com/Rahulns21). Feel free to contribute or report issues [here](https://github.com/Rahulns21/food-calorie-tracker/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



