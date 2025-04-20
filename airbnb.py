import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
# streamlit

st.set_page_config(layout="wide")
st.title("AIRBNB ANALYSIS")
st.write("")

df = pd.read_csv("S:\Projects\Airbnb\Airbnb.csv")

tab1,tab2 = st.tabs(["Home","Data Exploration"])
with tab1:
    image_air = Image.open("S:/Projects/Airbnb/Airbnb_Logo_Bélo.svg.png")
    st.image(image_air)
    st.header("About")
    st.write("")
    st.write("Airbnb is a popular online platform that connects people looking for accommodations with hosts offering unique spaces, ranging from apartments and houses to treehouses and castles.")
    st.write("It operates in over 220 countries and regions, making it a global leader in short-term rentals.")
    st.write("Founded in 2008 by Brian Chesky, Joe Gebbia, and Nathan Blecharczyk, Airbnb has revolutionized the hospitality industry by allowing individuals to rent out their homes, apartments, or even creative spaces like treehouses, boats, or yurts.")

    st.header("Key Features Of Airbnb")
    st.write("")
    st.markdown(""" - ***Wide Range of Listings:*** Airbnb offers everything from budget-friendly rooms to luxury villas, catering to different needs and budgets.""")
    st.markdown("""- ***Experiences:*** Beyond accommodations, Airbnb provides curated activities hosted by locals, such as cooking classes, guided tours, and adventure sports.""")
    st.markdown("""- ***Global Reach:*** Operating in over 220 countries, it gives travelers access to unique stays and cultural experiences across the globe.""")
    st.markdown(""" - ***Community-Based:*** It fosters a sense of community by connecting travelers with local hosts, creating personal and immersive stays.""")

with tab2:
    tab1,tab2,tab3,tab4 = st.tabs(["Price Analysis",
                                        "Availability Analysis",
                                        "Location Based Analysis",
                                        "Geospatial Visualization"
                                        ])
    
    with tab1:

        st.header("Price Variation")
        col1,col2 = st.columns(2)

        with col1:
            country = st.selectbox("Select The Country for Price Analysis",df['country'].unique())

            df_p_c = df[df['country'] == country]
            df_p_c.reset_index(drop=True,inplace=True)

            room = st.selectbox("Select The Room Type for Price Analysis",df['room_type'].unique())

            df_p_r = df_p_c[df_p_c['room_type'] == room]
            df_p_r.reset_index(drop=True,inplace=True)

            df_p_r_bar = df_p_r.groupby('property_type').agg({'price':'sum','review_scores':'mean','number_of_reviews':'sum'})
            df_p_r_bar.reset_index(inplace=True)

            df_p_r_bar_1 = px.bar(df_p_r_bar,x='property_type',y='price',title="Price Based On Property",hover_data=['number_of_reviews','review_scores'],width=600,height=500
                      ,color_discrete_sequence=px.colors.sequential.Bluyl)
            st.plotly_chart (df_p_r_bar_1)

        with col2:

            property = st.selectbox("Select The Property for Price Analysis",df_p_r['property_type'].unique())

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_p_p = df_p_r[df_p_r['property_type'] == property ]
            df_p_p.reset_index(drop = True, inplace = True)

            df_p_p_pie = df_p_p.groupby("host_response_time")[['price','bedrooms']].sum()
            df_p_p_pie.reset_index(inplace=True)

            df_p_p_pie_1 = px.pie(df_p_p_pie,names='host_response_time',values='price',hover_data='bedrooms',
                                  color_discrete_sequence=px.colors.sequential.Bluered,title="Price Difference Based On Host Response Time",
                                  width=600,height=500
                                  )
            st.plotly_chart(df_p_p_pie_1)
    
    with tab2:

        st.header("Availability Analysis")
        col1,col2 = st.columns(2)

        with col1:
            country = st.selectbox("Select The Country to know the availability",df['country'].unique())

            df_a_c = df[df['country'] == country]
            df_a_c.reset_index(drop=True,inplace=True)

            property = st.selectbox("Select The Property to know the availability",df_a_c['property_type'].unique())

            df_a_p = df_a_c[df_a_c['property_type'] == property ]
            df_a_p.reset_index(drop = True, inplace = True)

            df_a_sb_30 = px.sunburst(df_a_p,path=['room_type','bed_type','is_location_exact'],
                                  values='availability_30',width=600,height=500,title="Availability for 30 days",
                                  color_discrete_sequence=px.colors.sequential.Blugrn)
            
            st.plotly_chart(df_a_sb_30)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_a_sb_60 = px.sunburst(df_a_p,path=['room_type','bed_type','is_location_exact'],
                                  values='availability_60',width=600,height=500,title="Availability for 60 days",
                                  color_discrete_sequence=px.colors.sequential.Blugrn)
            
            st.plotly_chart(df_a_sb_60)
            
            
        col1,col2 = st.columns(2)

        with col1:

            df_a_sb_90 = px.sunburst(df_a_p,path=['room_type','bed_type','is_location_exact'],
                                  values='availability_90',width=600,height=500,title="Availability for 90 days",
                                  color_discrete_sequence=px.colors.sequential.Blugrn)
            
            st.plotly_chart(df_a_sb_90)
            
        with col2:

            df_a_sb_365 =  px.sunburst(df_a_p,path=['room_type','bed_type','is_location_exact'],
                                  values='availability_90',width=600,height=500,title="Availability for 365 days",
                                  color_discrete_sequence=px.colors.sequential.Blugrn)
            
            st.plotly_chart(df_a_sb_365)

        room = st.selectbox("Select The Room Type to know the Availability",df_a_p['room_type'].unique())

        df_a_r = df_a_p[df_a_p['room_type'] == room ]
        df_a_r.reset_index(drop = True, inplace = True)

        df_a_r_bar = df_a_r.groupby('host_response_time')[['availability_30','availability_60','availability_90','availability_365']].sum()
        df_a_r_bar.reset_index(inplace = True)

        df_a_r_bar_1 = px.bar(df_a_r_bar,x='host_response_time',y=['availability_30','availability_60','availability_90','availability_365'],
                              title="Availability based on Host response time",color_discrete_sequence=px.colors.sequential.algae,
                              barmode='group')
        
        st.plotly_chart(df_a_r_bar_1)

    with tab3:

        st.header("Location Based Analysis")
        st.write("")
        st.write("In this analysis, we are going to categorize the available spaces based on their prices.")
        st.write("30% of the value has the budget friendly listings")
        st.write("30%-60% of the value has the mid range listings")
        st.write("60%-100% of the value has the premium listings")
        st.write("The listings are categorized by their features, allowing users to view and select spaces based on their needs")

        st.write("")

        country = st.selectbox("Select the Country to view the ranges",df['country'].unique())

        df_lba_c = df[df['country']== country ]
        df_lba_c.reset_index(drop = True, inplace = True)

        prop = st.selectbox("Select the Property to view the ranges",df_lba_c['property_type'].unique())
        df_lba_p = df_lba_c[df_lba_c['property_type'] == prop ] 
        df_lba_p.reset_index(drop = True, inplace = True)

        max_min = df_lba_p['price'].max()- df_lba_p['price'].min()

        def value(sel_val):
        
            if sel_val == str(df_lba_p['price'].min()) + ' ' + str('to') + ' ' + str(max_min*0.30 + df_lba_p['price'].min()) + ' ' + str("(30% of the value)"):

                df_val_30 = df_lba_p[df_lba_p['price'] <= max_min*0.30 + df_lba_p['price'].min()]
                df_val_30.reset_index(drop = True, inplace = True)
                return df_val_30
            
            elif sel_val == str(max_min*0.30 + df_lba_p['price'].min()) + ' ' + str("to") + ' ' + str(max_min*0.60 + df_lba_p['price'].min()) + ' ' + str("(30% to 60% of the value)"):

                df_val_60 = df_lba_p[df_lba_p['price'] >= max_min*0.30 + df_lba_p['price'].min()]
                df_val_60_1 = df_val_60[df_val_60['price'] <= max_min*0.60 + df_lba_p['price'].min()]
                df_val_60_1.reset_index(drop = True, inplace = True)
                return df_val_60_1
            
            elif sel_val == str(max_min*0.60 + df_lba_p['price'].min()) + ' ' + str("to") + ' ' + str(df_lba_p['price'].max()) + ' ' + str("(60% to 100% of the value)"):
                
                df_val_100 = df_lba_p[df_lba_p['price'] >= max_min*0.60 + df_lba_p['price'].min()]
                df_val_100.reset_index(drop = True, inplace = True)
                return df_val_100
            
        value_selection = st.radio("Select the Price Range",[str(df_lba_p['price'].min()) + ' ' + str("to") + ' ' + str(max_min*0.30 + df_lba_p['price'].min()) + ' '+ str("(30% of the value)"),
                                                             str(max_min*0.30 + df_lba_p['price'].min()) + ' ' + str("to") + ' ' + str(max_min*0.60 + df_lba_p['price'].min()) + ' ' + str("(30% to 60% of the value)"),
                                                             str(max_min*0.60 + df_lba_p['price'].min()) + ' ' + str("to") + ' ' + str(df_lba_p['price'].max()) + ' ' + str("(60% to 100% of the value)")])
        
        df_value_selection = value(value_selection)

        st.dataframe(df_value_selection)


        df_value_selection_correlation = df_value_selection.drop(columns =["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()
        
        st.dataframe(df_value_selection_correlation)

        df_value_selection_correlation_g = pd.DataFrame(df_value_selection.groupby('accommodates')[['cleaning_fee','bedrooms','beds','extra_people']].sum())
        df_value_selection_correlation_g.reset_index(inplace=True)

        df_value_selection_correlation_g_bar_1 = px.bar(df_value_selection_correlation_g,x='accommodates',y=['cleaning_fee','bedrooms','beds','extra_people'],
                                                      title='Count of Accommodation',hover_data="extra_people",barmode='group',color_discrete_sequence=px.colors.sequential.Aggrnyl,
                                                      width=1000)
        
        st.plotly_chart(df_value_selection_correlation_g_bar_1)

        rt = st.selectbox("Select the room type",df_value_selection['room_type'].unique())
        df_value_selection_rt = df_value_selection[df_value_selection['room_type'] == rt]

        df_value_selection_rt_bar = px.bar(df_value_selection_rt,x=["street","host_location","host_neighbourhood"],y="market",title="",hover_data=['name','host_name','market'],
                                           barmode='group',color_discrete_sequence=px.colors.sequential.algae,width=1000,orientation='h')
        st.plotly_chart(df_value_selection_rt_bar)

        df_value_selection_rt_bar_2 = px.bar(df_value_selection_rt,x='government_area',y=['host_is_superhost','host_neighbourhood','cancellation_policy'],title="government_area",
                                             hover_data=['guests_included','location_type'],barmode='group',color_discrete_sequence=px.colors.sequential.amp,width=1000)
        st.plotly_chart(df_value_selection_rt_bar_2)

                                        

    with tab4:

        st.header("Geospatial Visualization")

        df_map = px.scatter_mapbox(df,lat='latitude',lon='longtitude',color='price',size='accommodates',
                                   color_continuous_scale='rainbow',hover_name='name',range_color=(0,49000),mapbox_style='carto-positron',
                                   zoom=1,width=1200,height=800,title="Global Airbnb Network")
        st.plotly_chart(df_map)

        
        




        

            













    



