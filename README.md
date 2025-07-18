# Airline Network Analysis ✈️

This project analyzes the global airline network to identify key airports using Social Network Analysis techniques. By processing flight route data, it highlights the strategic airports that function as major hubs and crucial intermediaries in the global air transportation system.

The analysis is based on the **OpenFlights dataset** and utilizes various Python libraries for data manipulation, network analysis, and visualization. The final report provides a detailed overview of the methodology and findings.

***

## 🌟 Key Findings

The analysis successfully identified two main categories of key airports by using **Degree Centrality** and **Betweenness Centrality**:

### 1. **High-Traffic Hubs (High Degree Centrality)**
These airports manage the highest volume of incoming and outgoing flights, acting as the most connected nodes in the network.
* **ATL** (Hartsfield-Jackson Atlanta International Airport)
* **ORD** (Chicago O'Hare International Airport)
* **LAX** (Los Angeles International Airport)

### 2. **Strategic Gatekeepers (High Betweenness Centrality)**
These airports are crucial "bridges" in the network, connecting distant geographical regions. They are vital for the resilience and efficiency of global air travel.
* **LAX** (Los Angeles International Airport)
* **SIN** (Singapore Changi Airport)
* **PEK** (Beijing Capital International Airport)
* **LHR** (London Heathrow Airport)

A moderately strong positive correlation (0.7646) was found between the two centrality measures, indicating that many highly connected airports also serve as strategic transit points.

***

## 📁 Repository Structure

This repository is organized into the following directories:

```
├── code/
│   ├── setup_environment.py
│   ├── data.py
│   └── library.py
├── dataset/
│   └── (contains the .csv files used)
├── plots/
│   └── (contains the generated plots and maps)
├── report/
│   └── Report.pdf
├── .gitignore
├── LICENSE
└── README.md
```

* **`code/`**: Contains all the Python scripts for the analysis.
* **`dataset/`**: Contains the raw and processed datasets.
* **`plots/`**: Stores all visualizations generated during the analysis.
* **`report/`**: Includes the final detailed project report in PDF format.

***

## 🚀 Getting Started

To replicate this analysis, follow these steps:

### Prerequisites
- Python 3.x
- Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Airline-Network-Analysis.git](https://github.com/YourUsername/Airline-Network-Analysis.git)
    cd Airline-Network-Analysis
    ```

2.  **Set up the environment:**
    Run the `setup_environment.py` script to install all the necessary Python libraries.
    ```bash
    python code/setup_environment.py
    ```

3.  **Configure Paths:**
    Before running the main analysis, you need to update the file paths in the scripts.
    * Open `code/data.py` and `code/library.py`.
    * Locate the placeholder comment: `# DEFINIRE PATH DATSET QUI #`.
    * Update the path to point to the location of the dataset on your local machine.
        * **Note:** In `data.py`, you need to update the path at the beginning of the script (for loading data) and at the end (for saving the output dataset).

4.  **Run the Analysis:**
    Once the paths are configured, you are ready to run the main analysis script.

***

## 🛠️ Tools and Libraries Used

* **Programming Language:** Python
* **Core Libraries:**
    * **Pandas:** For data manipulation and analysis.
    * **NumPy:** For numerical operations.
    * **NetworkX:** For creating, manipulating, and studying the network structure.
    * **Matplotlib, Seaborn, Cartopy:** For data visualization and creating geographical plots.

***

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgments
- The analysis is based on flight data from [OpenFlights.org](https://openflights.org/data.html).
- [cite_start]The project was developed as part of the Social Network Analysis course at Ca' Foscari University of Venice[cite: 5, 570].

---
*Created with ❤️ by Hakim Haddaoui*