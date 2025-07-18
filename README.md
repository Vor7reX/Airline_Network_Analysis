# Airline Network Analysis ✈️

This project analyzes the global airline network to identify key airports using Social Network Analysis techniques. By processing flight route data, it highlights the strategic airports that function as major hubs and crucial intermediaries in the global air transportation system.

The analysis is based on the **OpenFlights dataset** and utilizes various Python libraries for data manipulation, network analysis, and visualization. The final report provides a detailed overview of the methodology and findings.

![Visual representation of the global flight network](plot/world_plot.png)

***

## 🌟 Key Findings

The analysis successfully identified two main categories of key airports by using **Degree Centrality** and **Betweenness Centrality**:

### 1. **High-Traffic Hubs (High Degree Centrality)**
[cite_start]These airports manage the highest volume of incoming and outgoing flights, acting as the most connected nodes in the network[cite: 528, 529].
* [cite_start]**ATL** (Hartsfield-Jackson Atlanta International Airport) [cite: 532]
* [cite_start]**ORD** (Chicago O'Hare International Airport) [cite: 533]
* [cite_start]**LAX** (Los Angeles International Airport) [cite: 534]

### 2. **Strategic Gatekeepers (High Betweenness Centrality)**
[cite_start]These airports are crucial "bridges" in the network, connecting distant geographical regions[cite: 489, 537]. [cite_start]They are vital for the resilience and efficiency of global air travel[cite: 481].
* [cite_start]**LAX** (Los Angeles International Airport) [cite: 543]
* [cite_start]**SIN** (Singapore Changi Airport) [cite: 542]
* [cite_start]**PEK** (Beijing Capital International Airport) [cite: 541]
* [cite_start]**LHR** (London Heathrow Airport) [cite: 540]

[cite_start]A moderately strong positive correlation (0.7646) was found between the two centrality measures, indicating that many highly connected airports also serve as strategic transit points[cite: 491, 492].

***

## 📊 Visual Highlights

Here are some key visualizations from the analysis that illustrate the findings.

### Correlation between Degree and Betweenness Centrality
[cite_start]This plot shows the positive relationship between the number of connections an airport has (Degree) and its strategic importance as a bridge in the network (Betweenness)[cite: 491, 522].
![Scatter plot showing the correlation between Degree and Betweenness Centrality](plot/Scatter_Plot_with_Regression_and_Area.png)

### Top 50 Airports by Number of Routes
[cite_start]This bar chart clearly shows the dominance of airports like ATL and ORD, which have the highest number of flight routes[cite: 326].
![Bar chart of the top 50 airports by Degree Centrality](plot/Degree_Centrality_Bar_Chart_Top_50.png)

### The Network's Strategic Bridges
[cite_start]This map highlights the airports with the highest Betweenness Centrality, showing their crucial role in connecting different parts of the globe[cite: 473, 475].
![Map highlighting airports with high Betweenness Centrality](plot/Betweenness_Centrality.png)

***

## 📁 Repository Structure

This repository is organized into the following directories:

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


* **`code/`**: Contains all the Python scripts for the analysis.
* **`dataset/`**: Contains the raw and processed datasets.
* **`plots/`**: Stores all visualizations generated during the analysis.
* **`report/`**: Includes the final detailed project report in PDF format.

***

## 🚀 Getting Started

To replicate this analysis, follow these steps:

### Prerequisites
* Python 3.x
* Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Vor7reX/Airline-Network-Analysis.git](https://github.com/Vor7reX/Airline-Network-Analysis.git)
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

* [cite_start]**Programming Language:** Python [cite: 562]
* **Core Libraries:**
    * [cite_start]**Pandas:** For data manipulation and analysis[cite: 93, 564].
    * [cite_start]**NumPy:** For numerical operations[cite: 92, 563].
    * [cite_start]**NetworkX:** For creating, manipulating, and studying the network structure[cite: 94, 565].
    * [cite_start]**Matplotlib, Seaborn, Cartopy:** For data visualization and creating geographical plots[cite: 95, 96, 97, 566, 567, 568].

***

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgments
- [cite_start]The analysis is based on flight data from [OpenFlights.org](https://openflights.org/data.html)[cite: 560].
- [cite_start]The project was developed as part of the Social Network Analysis course at Ca' Foscari University of Venice[cite: 5, 570].

---
*Created with ❤️ by Hakim Haddaoui*
