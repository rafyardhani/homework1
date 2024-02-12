import requests
import math
import pandas as pd

url_target = 'https://gql.tokopedia.com/graphql/SearchProductQueryV4'
header = {
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'Tkpd-UserId': '0',
    'X-Version': '7f31f0d',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'Referer': 'https://www.tokopedia.com/search?st=product&q=&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=home,home',
    'X-Source': 'tokopedia-lite',
    'x-device': 'desktop-0.0',
    'X-Tkpd-Lite-Service': 'zeus',
    'sec-ch-ua-platform': '"Windows"'
}

def cek_data(keyword):
    init_query = f'[{{"operationName":"SearchProductQueryV4","variables":{{"params":"device=desktop&navsource=home&ob=23&page=1&q={keyword}&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=universe&srp_component_id=01.02.01.01&st=product&start=0&topads_bucket=true&unique_id=9472c4a105192230ca8895936f1e0d1d&user_addressId=&user_cityId=176&user_districtId=2274&user_id=&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants="}},"query":"query SearchProductQueryV4($params: String\u0021) {{\\n  ace_search_product_v4(params: $params) {{\\n    header {{\\n      totalData\\n      totalDataText\\n      processTime\\n      responseCode\\n      errorMessage\\n      additionalParams\\n      keywordProcess\\n      componentId\\n      __typename\\n    }}\\n    data {{\\n      banner {{\\n        position\\n        text\\n        imageUrl\\n        url\\n        componentId\\n        trackingOption\\n        __typename\\n      }}\\n      backendFilters\\n      isQuerySafe\\n      ticker {{\\n        text\\n        query\\n        typeId\\n        componentId\\n        trackingOption\\n        __typename\\n      }}\\n      redirection {{\\n        redirectUrl\\n        departmentId\\n        __typename\\n      }}\\n      related {{\\n        position\\n        trackingOption\\n        relatedKeyword\\n        otherRelated {{\\n          keyword\\n          url\\n          product {{\\n            id\\n            name\\n            price\\n            imageUrl\\n            rating\\n            countReview\\n            url\\n            priceStr\\n            wishlist\\n            shop {{\\n              city\\n              isOfficial\\n              isPowerBadge\\n              __typename\\n            }}\\n            ads {{\\n              adsId: id\\n              productClickUrl\\n              productWishlistUrl\\n              shopClickUrl\\n              productViewUrl\\n              __typename\\n            }}\\n            badges {{\\n              title\\n              imageUrl\\n              show\\n              __typename\\n            }}\\n            ratingAverage\\n            labelGroups {{\\n              position\\n              type\\n              title\\n              url\\n              __typename\\n            }}\\n            componentId\\n            __typename\\n          }}\\n          componentId\\n          __typename\\n        }}\\n        __typename\\n      }}\\n      suggestion {{\\n        currentKeyword\\n        suggestion\\n        suggestionCount\\n        instead\\n        insteadCount\\n        query\\n        text\\n        componentId\\n        trackingOption\\n        __typename\\n      }}\\n      products {{\\n        id\\n        name\\n        ads {{\\n          adsId: id\\n          productClickUrl\\n          productWishlistUrl\\n          productViewUrl\\n          __typename\\n        }}\\n        badges {{\\n          title\\n          imageUrl\\n          show\\n          __typename\\n        }}\\n        category: departmentId\\n        categoryBreadcrumb\\n        categoryId\\n        categoryName\\n        countReview\\n        customVideoURL\\n        discountPercentage\\n        gaKey\\n        imageUrl\\n        labelGroups {{\\n          position\\n          title\\n          type\\n          url\\n          __typename\\n        }}\\n        originalPrice\\n        price\\n        priceRange\\n        rating\\n        ratingAverage\\n        shop {{\\n          shopId: id\\n          name\\n          url\\n          city\\n          isOfficial\\n          isPowerBadge\\n          __typename\\n        }}\\n        url\\n        wishlist\\n        sourceEngine: source_engine\\n        __typename\\n      }}\\n      violation {{\\n        headerText\\n        descriptionText\\n        imageURL\\n        ctaURL\\n        ctaApplink\\n        buttonText\\n        buttonType\\n        __typename\\n      }}\\n      __typename\\n    }}\\n    __typename\\n  }}\\n}}\\n"}}]'
    response = requests.post(url_target, headers=header, data=init_query)
    jumlah_data = response.json()[0]['data']['ace_search_product_v4']['header']['totalData']
    jumlah_page = math.ceil(jumlah_data/60) + 1

    return jumlah_data, jumlah_page


def get_data(keyword):
    print("Please Wait")
    jml_data, jml_page = cek_data(keyword)
    hasil = []
    for page, data in zip(range(1, jml_page), range(0, jml_data, 60)):
        print(1*page)
        query= f'[{{"operationName":"SearchProductQueryV4","variables":{{"params":"device=desktop&navsource=home&ob=23&page={page}&q={keyword}&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=universe&srp_component_id=01.02.01.01&st=product&start={data}&topads_bucket=true&unique_id=9472c4a105192230ca8895936f1e0d1d&user_addressId=&user_cityId=176&user_districtId=2274&user_id=&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants="}},"query":"query SearchProductQueryV4($params: String\u0021) {{\\n  ace_search_product_v4(params: $params) {{\\n    header {{\\n      totalData\\n      totalDataText\\n      processTime\\n      responseCode\\n      errorMessage\\n      additionalParams\\n      keywordProcess\\n      componentId\\n      __typename\\n    }}\\n    data {{\\n      banner {{\\n        position\\n        text\\n        imageUrl\\n        url\\n        componentId\\n        trackingOption\\n        __typename\\n      }}\\n      backendFilters\\n      isQuerySafe\\n      ticker {{\\n        text\\n        query\\n        typeId\\n        componentId\\n        trackingOption\\n        __typename\\n      }}\\n      redirection {{\\n        redirectUrl\\n        departmentId\\n        __typename\\n      }}\\n      related {{\\n        position\\n        trackingOption\\n        relatedKeyword\\n        otherRelated {{\\n          keyword\\n          url\\n          product {{\\n            id\\n            name\\n            price\\n            imageUrl\\n            rating\\n            countReview\\n            url\\n            priceStr\\n            wishlist\\n            shop {{\\n              city\\n              isOfficial\\n              isPowerBadge\\n              __typename\\n            }}\\n            ads {{\\n              adsId: id\\n              productClickUrl\\n              productWishlistUrl\\n              shopClickUrl\\n              productViewUrl\\n              __typename\\n            }}\\n            badges {{\\n              title\\n              imageUrl\\n              show\\n              __typename\\n            }}\\n            ratingAverage\\n            labelGroups {{\\n              position\\n              type\\n              title\\n              url\\n              __typename\\n            }}\\n            componentId\\n            __typename\\n          }}\\n          componentId\\n          __typename\\n        }}\\n        __typename\\n      }}\\n      suggestion {{\\n        currentKeyword\\n        suggestion\\n        suggestionCount\\n        instead\\n        insteadCount\\n        query\\n        text\\n        componentId\\n        trackingOption\\n        __typename\\n      }}\\n      products {{\\n        id\\n        name\\n        ads {{\\n          adsId: id\\n          productClickUrl\\n          productWishlistUrl\\n          productViewUrl\\n          __typename\\n        }}\\n        badges {{\\n          title\\n          imageUrl\\n          show\\n          __typename\\n        }}\\n        category: departmentId\\n        categoryBreadcrumb\\n        categoryId\\n        categoryName\\n        countReview\\n        customVideoURL\\n        discountPercentage\\n        gaKey\\n        imageUrl\\n        labelGroups {{\\n          position\\n          title\\n          type\\n          url\\n          __typename\\n        }}\\n        originalPrice\\n        price\\n        priceRange\\n        rating\\n        ratingAverage\\n        shop {{\\n          shopId: id\\n          name\\n          url\\n          city\\n          isOfficial\\n          isPowerBadge\\n          __typename\\n        }}\\n        url\\n        wishlist\\n        sourceEngine: source_engine\\n        __typename\\n      }}\\n      violation {{\\n        headerText\\n        descriptionText\\n        imageURL\\n        ctaURL\\n        ctaApplink\\n        buttonText\\n        buttonType\\n        __typename\\n      }}\\n      __typename\\n    }}\\n    __typename\\n  }}\\n}}\\n"}}]'
        response = requests.post(url_target, headers=header, data=query)
        products = response.json()[0]['data']['ace_search_product_v4']['data']['products']
        hasil.extend(products)
    
    dtFrame = pd.DataFrame.from_dict(hasil)
    print("Data has been fetched")
    return dtFrame

def clean_data(keyword):
    dtFrame = get_data(keyword)
    df_expanded1 = pd.json_normalize(dtFrame['ads'])
    df_expanded2 = pd.json_normalize(dtFrame['shop'])
    col = df_expanded2.columns
    col = col.tolist()
    for i in range(len(col)):
        col[i] = "shop_"+col[i]
    df_expanded2 = df_expanded2.rename(columns=dict(zip(df_expanded2.columns, col)))
    
    df_result = pd.concat([dtFrame, df_expanded1, df_expanded2, df_expanded2], axis=1)

    df_result = df_result.drop(['ads', 'shop', 'badges'], axis=1)

    df_result = df_result.loc[:,~df_result.columns.duplicated()]
    df = pd.DataFrame()
    df['Nama Produk'] = df_result['name']
    df['Rating'] = df_result['rating']
    df['Nama Toko'] = df_result['shop_name']
    df['Lokasi Toko'] = df_result['shop_city']
    df['Jumlah Pembelian'] = df_result['countReview']
    df['Preview'] = df_result['imageUrl']
    df['Diskon'] = df_result['discountPercentage']
    df['Harga Normal'] = df_result['originalPrice']
    df['Harga Diskon'] = df_result['price']
    return df