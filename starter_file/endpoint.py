import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

data = {
    "data":
    [
        {
            'total_cases': "0",
            'total_deaths': "0",
            'new_deaths': "0",
            'new_deaths_smoothed': "0",
            'total_cases_per_million': "0",
            'total_deaths_per_million': "0",
            'new_deaths_per_million': "0",
            'new_deaths_smoothed_per_million': "0",
            'reproduction_rate': "0",
            'icu_patients': "0",
            'icu_patients_per_million': "0",
            'hosp_patients': "0",
            'new_tests': "0",
            'total_tests': "0",
            'total_tests_per_thousand': "0",
            'positive_rate': "0",
            'tests_per_case': "0",
            'stringency_index': "0",
            'population': "0",
            'population_density': "0",
            'median_age': "0",
            'aged_65_older': "0",
            'aged_70_older': "0",
            'gdp_per_capita': "0",
            'extreme_poverty': "0",
            'cardiovasc_death_rate': "0",
            'diabetes_prevalence': "0",
            'female_smokers': "0",
            'male_smokers': "0",
            'handwashing_facilities': "0",
            'hospital_beds_per_thousand': "0",
            'life_expectancy': "0",
            'human_development_index': "0",
            'testing_units': "0",
            'iso_code_AFG': "0",
            'iso_code_AGO': "0",
            'iso_code_AIA': "0",
            'iso_code_ALB': "0",
            'iso_code_AND': "0",
            'iso_code_ARE': "0",
            'iso_code_ARG': "0",
            'iso_code_ARM': "0",
            'iso_code_ATG': "0",
            'iso_code_AUS': "0",
            'iso_code_AUT': "0",
            'iso_code_AZE': "0",
            'iso_code_BDI': "0",
            'iso_code_BEL': "0",
            'iso_code_BEN': "0",
            'iso_code_BFA': "0",
            'iso_code_BGD': "0",
            'iso_code_BGR': "0",
            'iso_code_BHR': "0",
            'iso_code_BHS': "0",
            'iso_code_BIH': "0",
            'iso_code_BLR': "0",
            'iso_code_BLZ': "0",
            'iso_code_BMU': "0",
            'iso_code_BOL': "0",
            'iso_code_BRA': "0",
            'iso_code_BRB': "0",
            'iso_code_BRN': "0",
            'iso_code_BTN': "0",
            'iso_code_BWA': "0",
            'iso_code_CAF': "0",
            'iso_code_CAN': "0",
            'iso_code_CHE': "0",
            'iso_code_CHL': "0",
            'iso_code_CHN': "0",
            'iso_code_CIV': "0",
            'iso_code_CMR': "0",
            'iso_code_COD': "0",
            'iso_code_COG': "0",
            'iso_code_COL': "0",
            'iso_code_COM': "0",
            'iso_code_CPV': "0",
            'iso_code_CRI': "0",
            'iso_code_CUB': "0",
            'iso_code_CYM': "0",
            'iso_code_CYP': "0",
            'iso_code_CZE': "0",
            'iso_code_DEU': "0",
            'iso_code_DJI': "0",
            'iso_code_DMA': "0",
            'iso_code_DNK': "0",
            'iso_code_DOM': "0",
            'iso_code_DZA': "0",
            'iso_code_ECU': "0",
            'iso_code_EGY': "0",
            'iso_code_ERI': "0",
            'iso_code_ESP': "0",
            'iso_code_EST': "0",
            'iso_code_ETH': "0",
            'iso_code_FIN': "0",
            'iso_code_FJI': "0",
            'iso_code_FLK': "0",
            'iso_code_FRA': "0",
            'iso_code_FRO': "0",
            'iso_code_FSM': "0",
            'iso_code_GAB': "0",
            'iso_code_GBR': "0",
            'iso_code_GEO': "0",
            'iso_code_GGY': "0",
            'iso_code_GHA': "0",
            'iso_code_GIB': "0",
            'iso_code_GIN': "0",
            'iso_code_GMB': "0",
            'iso_code_GNB': "0",
            'iso_code_GNQ': "0",
            'iso_code_GRC': "0",
            'iso_code_GRD': "0",
            'iso_code_GRL': "0",
            'iso_code_GTM': "0",
            'iso_code_GUY': "0",
            'iso_code_HKG': "0",
            'iso_code_HND': "0",
            'iso_code_HRV': "0",
            'iso_code_HTI': "0",
            'iso_code_HUN': "0",
            'iso_code_IDN': "0",
            'iso_code_IMN': "0",
            'iso_code_IND': "0",
            'iso_code_IRL': "0",
            'iso_code_IRN': "0",
            'iso_code_IRQ': "0",
            'iso_code_ISL': "0",
            'iso_code_ISR': "0",
            'iso_code_ITA': "0",
            'iso_code_JAM': "0",
            'iso_code_JEY': "0",
            'iso_code_JOR': "0",
            'iso_code_JPN': "0",
            'iso_code_KAZ': "0",
            'iso_code_KEN': "0",
            'iso_code_KGZ': "0",
            'iso_code_KHM': "0",
            'iso_code_KNA': "0",
            'iso_code_KOR': "0",
            'iso_code_KWT': "0",
            'iso_code_LAO': "0",
            'iso_code_LBN': "0",
            'iso_code_LBR': "0",
            'iso_code_LBY': "0",
            'iso_code_LCA': "0",
            'iso_code_LIE': "0",
            'iso_code_LKA': "0",
            'iso_code_LSO': "0",
            'iso_code_LTU': "0",
            'iso_code_LUX': "0",
            'iso_code_LVA': "0",
            'iso_code_MAC': "0",
            'iso_code_MAR': "0",
            'iso_code_MCO': "0",
            'iso_code_MDA': "0",
            'iso_code_MDG': "0",
            'iso_code_MDV': "0",
            'iso_code_MEX': "0",
            'iso_code_MHL': "0",
            'iso_code_MKD': "0",
            'iso_code_MLI': "0",
            'iso_code_MLT': "0",
            'iso_code_MMR': "0",
            'iso_code_MNE': "0",
            'iso_code_MNG': "0",
            'iso_code_MOZ': "0",
            'iso_code_MRT': "0",
            'iso_code_MSR': "0",
            'iso_code_MUS': "0",
            'iso_code_MWI': "0",
            'iso_code_MYS': "0",
            'iso_code_NAM': "0",
            'iso_code_NER': "0",
            'iso_code_NGA': "0",
            'iso_code_NIC': "0",
            'iso_code_NLD': "0",
            'iso_code_NOR': "0",
            'iso_code_NPL': "0",
            'iso_code_NZL': "0",
            'iso_code_OMN': "0",
            'iso_code_OWID_AFR': "0",
            'iso_code_OWID_ASI': "0",
            'iso_code_OWID_CYN': "0",
            'iso_code_OWID_EUN': "0",
            'iso_code_OWID_EUR': "0",
            'iso_code_OWID_INT': "0",
            'iso_code_OWID_KOS': "0",
            'iso_code_OWID_NAM': "0",
            'iso_code_OWID_OCE': "0",
            'iso_code_OWID_SAM': "0",
            'iso_code_OWID_WRL': "0",
            'iso_code_PAK': "0",
            'iso_code_PAN': "0",
            'iso_code_PER': "0",
            'iso_code_PHL': "0",
            'iso_code_PNG': "0",
            'iso_code_POL': "0",
            'iso_code_PRT': "0",
            'iso_code_PRY': "0",
            'iso_code_PSE': "0",
            'iso_code_QAT': "0",
            'iso_code_ROU': "0",
            'iso_code_RUS': "0",
            'iso_code_RWA': "0",
            'iso_code_SAU': "0",
            'iso_code_SDN': "0",
            'iso_code_SEN': "0",
            'iso_code_SGP': "0",
            'iso_code_SHN': "0",
            'iso_code_SLB': "0",
            'iso_code_SLE': "0",
            'iso_code_SLV': "0",
            'iso_code_SMR': "0",
            'iso_code_SOM': "0",
            'iso_code_SRB': "0",
            'iso_code_SSD': "0",
            'iso_code_STP': "0",
            'iso_code_SUR': "0",
            'iso_code_SVK': "0",
            'iso_code_SVN': "0",
            'iso_code_SWE': "0",
            'iso_code_SWZ': "0",
            'iso_code_SYC': "0",
            'iso_code_SYR': "0",
            'iso_code_TCA': "0",
            'iso_code_TCD': "0",
            'iso_code_TGO': "0",
            'iso_code_THA': "0",
            'iso_code_TJK': "0",
            'iso_code_TLS': "0",
            'iso_code_TTO': "0",
            'iso_code_TUN': "0",
            'iso_code_TUR': "0",
            'iso_code_TWN': "0",
            'iso_code_TZA': "0",
            'iso_code_UGA': "0",
            'iso_code_UKR': "0",
            'iso_code_URY': "0",
            'iso_code_USA': "0",
            'iso_code_UZB': "0",
            'iso_code_VAT': "0",
            'iso_code_VCT': "0",
            'iso_code_VEN': "0",
            'iso_code_VNM': "0",
            'iso_code_VUT': "0",
            'iso_code_WSM': "0",
            'iso_code_YEM': "0",
            'iso_code_ZAF': "0",
            'iso_code_ZMB': "0",
            'iso_code_ZWE': "0",
            'continent_0': "0",
            'continent_Africa': "0",
            'continent_Asia': "0",
            'continent_Europe': "0",
            'continent_North America': "0",
            'continent_Oceania': "0",
            'continent_South America': "0",
        },
    ],
}

body = str.encode(json.dumps(data))

url = 'http://b9138058-bfe9-4d78-a97b-b1a37ef287a5.eastus2.azurecontainer.io/score'
api_key = '4hU0ujUZdVfVfGqkLfI08Kuu3jDpb8Xb' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))