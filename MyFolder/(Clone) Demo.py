# Databricks notebook source
# MAGIC %sql
# MAGIC select 'Hi';

# COMMAND ----------

# MAGIC %run ./setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

File = dbutils.fs.ls('/databricks-datasets')
display(File)
