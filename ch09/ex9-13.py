dummies_df = pd.get_dummies(
    mailed_df[["zip_code", "channel"]], drop_first=True)
feature_vector_df = \
   mailed_df.drop(
       ["history_segment", "zip_code", "channel",
        "segment", "visit", "conversion", "spend"],
       axis=1)
feature_vector_df = feature_vector_df.join(dummies_df)
feature_vector_df.head(10)
