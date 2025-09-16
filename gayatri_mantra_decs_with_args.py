def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(11)
def gayatri_mantra(a):
    print("""ॐ भूर्भुवः स्वः 
तत्स॑वि॒तुर्वरे॑ण्यं॒  
भर्गो॑ दे॒वस्य॑ धीमहि।  
धियो॒ यो नः॑ प्रचो॒दया॑त्॥ 
""")
gayatri_mantra(None)