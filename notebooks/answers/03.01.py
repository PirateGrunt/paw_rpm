x.std() / x.mean()


# remove zero rows
triangle_frame = triangle_frame.groupby(level=0).filter(lambda x : np.nansum(x)  > 0)

# ata factors
ata_df = pd.DataFrame(triangle_frame.iloc[:, 1:].values / \
	triangle_frame.iloc[:, :-1].values, index=triangle_frame.index, columns=range(1,10))

# ldfs with default 1
ldf_df = ata_df.groupby(level=0).mean().fillna(1.)

# cdfs
cdf_df = ldf_df.sort_index(axis=1, ascending=False).cumprod(axis=1).sort_index(axis=1)

# diagonal
diag_df = triangle_frame.groupby(level=0).apply(
	lambda x : pd.Series(np.diagonal(x.values[:, ::-1])[::-1], index=range(1,11)))

# ultimate and ibnr
ult_df = (diag_df * cdf_df).fillna(0)
ibnr_df = ult_df - diag_df
