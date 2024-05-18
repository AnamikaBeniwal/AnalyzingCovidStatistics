# Analyzing COVID-19 Statistics

This project is designed to scrape COVID-19 case data from the WHO website, process it, and visualize it using a pie chart. 
The data includes total cases and cases for specific countries, with units converted to integers for accurate representation.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)

## Introduction
The goal of this project is to extract COVID-19 data from the World Health Organization (WHO) website, convert the data into a usable format, 
and create a pie chart to visualize the distribution of COVID-19 cases across different countries.

## Features
- Scrape data from the WHO website.
- Convert data values with units (e.g., 'm' for millions) into integers.
- Visualize the data using a pie chart with `matplotlib`.

## Installation
To run this project, you need to have Python installed along with several packages. You can install the necessary packages using the following commands:

```bash
pip install selenium
pip install beautifulsoup4
pip install html5lib
pip install matplotlib
