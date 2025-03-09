 Real-Time Network Metrics Dashboard

This project is a web-based dashboard designed to provide real-time visualization of key network metrics. It offers a simple, customizable, and user-friendly interface for monitoring network performance.

 Features

-   Real-time Chart Updates: Displays live charts for packet loss, latency, packet gain, and CPU usage.
-   Metric Selection: Allows users to select which metric to display.
-   Chart Type Customization: Users can choose between line, bar, and scatter charts.
-   Summary Statistics: Provides average, standard deviation, minimum, and maximum values for each metric.
-   Data Export: Enables data export in CSV and JSON formats.
-   Chart Download: Allows users to download the chart as a PNG image.
-   Theme Toggling: Users can switch between light and dark themes.
-   Responsive Design: Ensures the dashboard looks great on all screen sizes.

 Technologies Used

-   Python (Flask): Backend server and data processing.
-   SQLite: Lightweight database for storing metric data.
-   JavaScript (Chart.js): Real-time chart visualization.
-   HTML/CSS: User interface design.

 Getting Started

 Prerequisites

-   Python 3.x
-   A web browser (Chrome, Firefox, Edge, etc.)

 Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/yourusername/network-metrics-dashboard.git](https://github.com/yourusername/network-metrics-dashboard.git)
    cd network-metrics-dashboard
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate   On macOS/Linux
    venv\Scripts\activate   On Windows
    ```

3.  Install dependencies:

    ```bash
    pip install Flask
    ```

4.  Run the application:

    ```bash
    python visualize.py
    ```

5.  Open the dashboard in your browser:

    -   Navigate to `http://127.0.0.1:5000/` in your web browser.

 Usage

-   Use the dropdown menus to select the desired metric and chart type.
-   View the real-time charts and summary statistics.
-   Click the "Export CSV" or "Export JSON" buttons to download the data.
-   Click the "Download Chart" button to download the chart image.
-   Click the "Toggle Theme" button to switch between light and dark themes.

 File Structure

network-metrics-dashboard/
├── visualize.py       # Flask application
├── templates
     	├── index.html         # HTML frontend
	├── styles.css         # CSS styles
├── metrics.db         # SQLite database
├── README.md          # Project documentation
├── .gitignore         # Files to ignore by Git

Future Enhancements

-   Add more network metrics (jitter, throughput, etc.).
-   Implement an alerting and notification system.
-   Add user authentication and authorization.
-   Expand graphing options and data export formats.
-   Implement the use of web sockets.

Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details.