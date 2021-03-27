import pandas as pd
users = pd.read_csv ('users.csv')
purchases = pd.read_csv ('purchases.csv')

#Alternative 1
df = purchases.merge (users, how = "inner", on = "uid")

# Step 2. What are the total earnings in the breakdown of country, device, gender, age?

new_df = df.groupby (["country", "device", "gender", "age"]). agg (("price": sum})
new_df.head ()

# Step 3. We will be descending sort_values method into code to see the output better
# Apply according to price in the figure. Save the output as agg_df.

agg_df = new_df.sort_values(by = "price", ascending = False)
agg_df.head ()

# Step 4. Convert agg_df's indexes to variable name.
# (All variables except price in the output of the third question are index names)

agg_df = agg_df.reset_index ()
agg_df.head ()

# Step 5. Convert age variable to categorical variable
# and add it to agg_df with the name "age_cat".
# you can translate but it should be persuasive

agg_df ["age_cat"] = pd.cut (agg_df ["age"], bins = [0, 18, 23, 30, 40, 75], labels = ['0_18', '19_23', '24_30', ' 31_40 ',' 41_75 '])

agg_df.head ()


# Step 6. Define new level based customers and add them to the data set as variables.
# Categorical breakdowns in the data set according to the output you obtained in the previous question.
# Think of them as customer groups and identify new customers by combining these groups.

agg_df ["customer_level_based"] = [row [0] + "_" + row [1] .upper () + "_" + row [2] + "_" + row [5] for row in agg_df.values]
agg_df.head ()


# Step 7. Segment new customers by price,
# Add it to agg_df with the "segment" naming. Describe the segments.

agg_df = agg_df [["customer_level_based", "price"]]
agg_df.head ()

agg_df = agg_df.groupby ("customer_level_based").agg(("price": "mean"})
agg_df.reset_index (inplace = True)

agg_df ["segment"] = pd.qcut (agg_df ["price"], 4, labels = ["D", "C", "B", "A"])
agg_df.groupby ("segment").agg(("price":"mean"}).reset_index (inplace = True)
agg_df.head ()

# agg_df.groupby ("segment"). agg (("segment": "count"})

# Step 8. What segment is a 42-year-old Turkish woman using IOS in?
#Express the segment (group) of this person according to the # agg_df table.

new_customer = agg_df [agg_df ["customer_level_based"] == "TUR_IOS_F_41_75"]
new_customer