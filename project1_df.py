#dataframe structures
import dask.dataframe as dd
import numpy as np
import random

# %%
df = dd.read_csv("heart_failure_clinical_records_dataset.csv", assume_missing=True)
df.head()

# %%
# Check for missing values: this is a clean dataset
df.isnull().sum().compute()

# %%
# check descriptive statistics
df.describe().compute()

# %%
# plot the data, compare betweeen death events
import matplotlib.pyplot as plt
import seaborn as sns
fig, axs = plt.subplots(ncols=3, figsize=(15, 7))
sns.boxplot(x = 'DEATH_EVENT', y = 'age', data = df.compute(), ax = axs[0])
sns.boxplot(x = 'DEATH_EVENT', y = 'time', data = df.compute(), ax = axs[1])
sns.boxplot(x = 'DEATH_EVENT', y = 'ejection_fraction', data = df.compute(), ax = axs[2])
sns.displot(data=df, x="diabetes", hue="DEATH_EVENT", multiple="dodge", shrink=1.5)


# %%
# see correlation between variables, check correlation between each variable and DEATH_EVENT:
# target variables include: ejection_fraction, serum_creatinine, serum_sodium, time
df.corr().compute()


# %%
# write a fuccntion to get average
def get_average(status, variable):
    a = df[df.DEATH_EVENT == status][variable].mean().compute()
    return f'average {variable} for death event = {status} is {a}'


# command line interface
import click
@click.command()
@click.argument('status', type=int)
@click.argument('variable')
def call_get_average(status, variable):
    print(get_average(status, variable))

if __name__ == '__main__':
    call_get_average()

