from B_C_WEB_SITE import B_C_WEB_SITE

bc_website = B_C_WEB_SITE()

print(bc_website.GET_NUM_ROWS())
#%%
all_rucs = bc_website.GET_ALL_RUCS()

#%%
num_page_error = bc_website.CRAWLING_TEST()