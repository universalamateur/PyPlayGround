#!/usr/bin/env python3

import json
import locale
import sys
import os
from reports import generate as report
from emails import generate as email_generate
from emails import send as email_send


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  max_year = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    # Calculate the car model which had the most sales by completing the process_data method, and then appending a formatted string to the summary list
    if item["total_sales"]>max_sales["total_sales"]:
        max_sales = item
    # TODO: also handle most popular car_year
    # Calculate the most popular car_year across all car make/models (in other words, find the total count of cars with the car_year equal to 2005, equal to 2006, etc. and then figure out the most popular year) by completing the process_data method, and append a formatted string to the summary list
    max_year[str(item["car"]["car_year"])]=max_year.get(str(item["car"]["car_year"]), 0) + item["total_sales"]
  print(max_year)
  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(
      format_car(max_sales["car"]), max_sales["total_sales"]),
    "The most popular year was {} with {} sales.".format(
      max(max_year, key=lambda key: max_year[key]), max_year[str(max(max_year, key=lambda key: max_year[key]))]),
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  new_summary = '<br/>'.join(summary)
  new2_summary = '\n'.join(summary)
  # TODO: turn this into a PDF report
  path_pdf=os.path.abspath(os.path.join(os.sep, "tmp","cars.pdf"))
  report(path_pdf, "Cars report", new_summary, cars_dict_to_table(data))
  # TODO: send the PDF report as an email attachment
  msg = email_generate("automation@example.com", "student-01-89511c72f289@example.com", "Sales summary for last month", new2_summary, path_pdf)
  email_send(msg)

if __name__ == "__main__":
  main(sys.argv)
