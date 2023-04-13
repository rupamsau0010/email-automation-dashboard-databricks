# Databricks notebook source
# DBTITLE 1,Run to mount ADLS Gen2
v_result = dbutils.notebook.run("../connection_setup/connect-adls-gen2", 600)
print(v_result)

# COMMAND ----------

# DBTITLE 1,Run to connect Azure SQL DB
v_result = dbutils.notebook.run("../connection_setup/connect-with-azure-sql", 600)
print(v_result)

# COMMAND ----------

# DBTITLE 1,Run to transform and load manager's provided data
v_result = dbutils.notebook.run("../transformation_and_action/task_data_transformation_submitted_by_managers", 600)
print(v_result)

# COMMAND ----------

# DBTITLE 1,Run to transform and load employee's provided data
v_result = dbutils.notebook.run("../transformation_and_action/task_status_transformation_update_by_employees", 600)
print(v_result)

# COMMAND ----------

# DBTITLE 1,Run to trigger email for necessary getters
v_result = dbutils.notebook.run("../transformation_and_action/daily_scheduled_mail", 600)
print(v_result)

# COMMAND ----------

dbutils.notebook.exit("success")
