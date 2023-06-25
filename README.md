# Samee
# Samee - Virtual Sleep Assistant

![Samee Logo](samee_logo.png)

Samee (Sleep Assistant Meets Electronic Encouragement) is a virtual sleep assistant designed to help you complete your sleep routines and improve your sleep habits. Whether you're struggling with falling asleep, maintaining a consistent sleep schedule, or need guidance on establishing a healthy nighttime routine, Samee is here to assist you.

## Features

1. **Sign-In**: Start by signing in with your username and password to access personalized features and track your progress.

2. **Personal Information**: Set your personal information to receive customized sleep recommendations and connect with your caregivers. Provide details such as your date of birth, gender, height, weight, allergies, medications, medical conditions, and caregiver contact information.

3. **Set Your Routine**: Establish your ideal sleep routine by answering a series of questions. Specify your desired bedtime and wake-up time, and Samee will calculate the recommended sleep duration. You can also opt for bedtime reminders and create a personalized night routine with various activities.

4. **Prepare for Sleep**: Follow the instructions and complete tasks to prepare for bed. Samee will guide you through activities such as setting out clothes for tomorrow, brushing your teeth, washing your face, and more. Each task is accompanied by a countdown timer to help you manage your time effectively.

5. **Past Sleeps**: Track your sleep duration and view your progress over the past 100 days. A line chart visually represents your sleep duration, allowing you to identify patterns and work towards more consistent sleep habits.

6. **Additional Sources**: Explore additional personalized sleep resources to enhance your sleep knowledge. Samee provides personalized recommendations based on your profile and offers prescribed readings from reputable sources. You can also request more resources from your care provider if needed.

## Getting Started

To run the Samee app locally, follow these steps:

1. Install the required dependencies by running the following command:

   ```shell
   pip install streamlit streamlit_extras
   ```

2. Save the code provided in the respective files:
   - `sign_in.py`: Handles the sign-in functionality.
   - `personal_info.py`: Sets up and saves the user's personal information.
   - `set_routine.py`: Guides the user through setting up their sleep routine.
   - `prepare_for_sleep.py`: Helps the user prepare for bed with timed tasks.
   - `past_sleeps.py`: Displays the user's sleep duration over the past 100 days.
   - `additional_sources.py`: Provides additional sleep resources.

3. Run the Streamlit app by executing the following command in your terminal:

   ```shell
   streamlit run sign_in.py
   ```

4. Access the app in your web browser using the provided URL.

## Dependencies

The Samee app relies on the following dependencies:

- `streamlit`: The core library used to create the web application.
- `streamlit_extras`: Provides the rain effect used in the Prepare for Sleep section.

You can install the dependencies manually using `pip` or by including them in your project's `requirements.txt` file.

## Support

If you encounter any issues or have any questions or feedback, please reach out to our support team at support@samee.com. We are here to help you!

## License

The Samee app is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use the code for your own purposes.

---

Thank you for choosing Samee as your virtual sleep assistant! We hope it helps you establish healthy sleep habits and improve your overall well-being. Sleep well!
