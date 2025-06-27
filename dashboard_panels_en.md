# Grafana Panels for Cybersecurity Analysis

Below are the specific panels that can be created for each of the dashboard ideas, using the `nics_demo_flat.json` file as a data source in Grafana Infinity.

---

## 1. Cybersecurity Posture Overview

### Panels:

1.  **Overall Function Score (5 Gauge Panels)**
    *   **Panel Type:** Gauge
    *   **Data:** `function_score`
    *   **Configuration:** Create one panel for each of the 5 functions (`IDENTIFY`, `PROTECT`, `DETECT`, `RESPOND`, `RECOVER`).
        *   **Query:** Filter by the function name (e.g., `function == "IDENTIFY (ID)"`) and select the `function_score` field.
        *   **Visualization:** Set color thresholds: Red (0-60), Yellow (61-80), Green (81-100).

2.  **Scores by Category (Bar Chart)**
    *   **Panel Type:** Bar Chart
    *   **Data:** `category`, `category_score`
    *   **Configuration:**
        *   **Query:** Select the `category` and `category_score` fields. Group by `category` to ensure each bar represents a unique category.
        *   **Visualization:** Use the `category` field on the X-axis and `category_score` on the Y-axis. You can group by `function` to color the bars according to the function they belong to.

3.  **Scores Table (Table)**
    *   **Panel Type:** Table
    *   **Data:** `function`, `category`, `subcategory`, `category_score`, `subcategory_score`
    *   **Configuration:**
        *   **Query:** Select all relevant fields.
        *   **Visualization:** Display the columns in the desired order. Allow sorting by `category_score` and `subcategory_score` to quickly identify the lowest-performing areas. Use color thresholds on the score cells for quick visual identification.

---

## 2. Maturity Analysis by Domain

### Panels:

1.  **Maturity Radar by Category (Radar Chart)**
    *   **Panel Type:** Radar Chart or similar (Polystat).
    *   **Data:** `policy_score`, `process_score`, `implementation_score`, `measured_score`, `managed_score`
    *   **Configuration:**
        *   **Query:** Select a specific `category` (a Grafana variable can be used to allow the user to choose the category).
        *   **Visualization:** Each axis of the radar will represent a maturity level (Policy, Process, etc.), and the value will be the average score for that category.

2.  **Maturity Heatmap (Heatmap)**
    *   **Panel Type:** Heatmap
    *   **Data:** `subcategory`, maturity levels, and their scores.
    *   **Configuration:**
        *   **Query:** Select `subcategory` and all maturity score columns (`policy_score`, `process_score`, etc.).
        *   **Visualization:** The Y-axis will be the `subcategory`, the X-axis the 5 maturity levels, and the cell color will represent the score. This allows for a quick view of which maturity aspects are weakest overall.

3.  **Detailed Maturity Table (Table)**
    *   **Panel Type:** Table
    *   **Data:** `category`, `subcategory`, and all maturity columns (`policy_maturity`, `policy_score`, etc.).
    *   **Configuration:**
        *   **Query:** Select all relevant fields.
        *   **Visualization:** Display both the maturity level (e.g., "Fully Compliant") and the score. Use color thresholds on the score cells.

---

## 3. Effort vs. Score Analysis (Quick Wins)

### Panels:

1.  **Effort vs. Score Scatter Plot (Scatter Plot)**
    *   **Panel Type:** Scatter Plot
    *   **Data:** `estimated_level_of_effort_in_hours`, `subcategory_score`, `subcategory`
    *   **Configuration:**
        *   **Query:** Select the mentioned fields.
        *   **Visualization:** X-axis: `estimated_level_of_effort_in_hours`. Y-axis: `subcategory_score`. Each point is a `subcategory`. Points in the bottom-left corner are the "quick wins".

2.  **Prioritization Table (Table)**
    *   **Panel Type:** Table
    *   **Data:** `subcategory`, `subcategory_score`, `estimated_level_of_effort_in_hours`
    *   **Configuration:**
        *   **Query:** Select the fields and add a calculated column for the "Priority Index" (`subcategory_score` / `estimated_level_of_effort_in_hours`).
        *   **Visualization:** Sort the table by the priority index in ascending order to see the most efficient tasks first.

---

## 4. Risk Register View

### Panels:

1.  **Registered Risks Table (Table)**
    *   **Panel Type:** Table
    *   **Data:** `function`, `category`, `subcategory`, `risk_register`
    *   **Configuration:**
        *   **Query:** Filter where `risk_register` is not null.
        *   **Visualization:** Display the columns to clearly identify where risks have been registered.

2.  **Total Risks Counter (Stat)**
    *   **Panel Type:** Stat / Singlestat
    *   **Data:** Count of `risk_register`
    *   **Configuration:**
        *   **Query:** Count the number of records where `risk_register` is not null.
        *   **Visualization:** Display a large, clear number.

3.  **Risks by Function (Bar Chart)**
    *   **Panel Type:** Bar Chart
    *   **Data:** `function`, count of `risk_register`
    *   **Configuration:**
        *   **Query:** Group by `function` and count the records where `risk_register` is not null.
        *   **Visualization:** Show the number of risks for each cybersecurity function.

---

## 5. Compliance and Artifacts Status

### Panels:

1.  **Artifacts Status (Pie Chart)**
    *   **Panel Type:** Pie Chart
    *   **Data:** `artifacts_placed_in_folder`
    *   **Configuration:**
        *   **Query:** Group by `artifacts_placed_in_folder` and count the values (`Y` vs. `N`/null).
        *   **Visualization:** Show the percentage of subcategories that have the necessary documentation.

2.  **Artifact Gaps Table (Table)**
    *   **Panel Type:** Table
    *   **Data:** `function`, `category`, `subcategory`, `artifacts_needed`
    *   **Configuration:**
        *   **Query:** Filter where `artifacts_placed_in_folder` is 'N' or null.
        *   **Visualization:** List the areas where documentation is missing, along with the description of what is needed (`artifacts_needed`).

3.  **Missing Artifacts Counter (Stat)**
    *   **Panel Type:** Stat / Singlestat
    *   **Data:** Count of `artifacts_placed_in_folder`
    *   **Configuration:**
        *   **Query:** Count the number of records where `artifacts_placed_in_folder` is 'N' or null.
        *   **Visualization:** Display a large number for quick visual impact.

---

## 6. Detailed Subcategory Explorer

### Panels:

1.  **Master Subcategory Table (Table)**
    *   **Panel Type:** Table
    *   **Data:** All fields from the flattened JSON.
    *   **Configuration:**
        *   **Query:** Select all fields (`*`).
        *   **Visualization:** This panel is for exploration. Enable Grafana's table search and filtering functionality. The user will be able to type to search any field and use the table's filtering options for ad-hoc analysis. "Overrides" can be used to color score cells or format text.
