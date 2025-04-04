Pan Card Tampering Detection
📌 Project Overview
Pan Card Tampering Detection is a web-based application that analyzes PAN card images to detect modifications or tampering. By using computer vision and image similarity techniques, the application compares an uploaded image against an original version and highlights the differences. This project is useful for verifying document authenticity and preventing fraud.

The application is built with Flask for the backend and utilizes OpenCV and scikit-image for image processing. Deployment is handled via Railway, and version control is managed with Git and GitHub.

🚀 Features

✅ Upload an image of a PAN card

✅ Compare it against an original reference image

✅ Identify differences using structural similarity (SSIM)

✅ Highlight tampered areas using OpenCV contour detection

✅ Display results with a percentage match score

🛠 Technologies Used

🔹 Flask (Python Web Framework)
Flask is used as the web framework to handle user requests, file uploads, and image processing logic. It enables a simple yet powerful backend architecture for our application.

🔹 OpenCV (Computer Vision Library)
OpenCV allows us to process and analyze images, detect differences, and apply contour-based bounding boxes to highlight modifications.

🔹 scikit-image (Image Processing Library)
We use the structural similarity index (SSIM) from skimage.metrics to compute how similar two images are, helping to detect changes in a tampered document.

🔹 Jinja2 (Templating Engine for Flask)
Jinja2 is used to dynamically generate HTML pages, displaying the results of the tampering detection in a user-friendly way.

🔹 Materialize CSS (Frontend UI Framework)
Materialize CSS is used for styling and responsive UI components, making the application visually appealing and easy to use.

🔹 Git & GitHub (Version Control)
Git is used for tracking changes in the codebase, ensuring smooth collaboration and version control.

🔹 Railway (Cloud Deployment Platform)
Railway is used to deploy the Flask application to the cloud, making it accessible online. It provides an easy, scalable, and automated way to run the project without worrying about server management.


🌍 Live Deployment

This application is deployed on Railway, making it accessible online. You can test it at:
🔗 https://pancardtampering-production.up.railway.app/

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Developed by Ruben Pinheiro
