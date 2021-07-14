import pandas as pd
import creme


def get_all_attributes(package):
    subpackages = []
    submodules = []
    for module in package.__all__:
        subpackages.append(module)
        submodules.append(getattr(package, module).__all__)
    df = pd.DataFrame(submodules)
    df = df.T
    df.columns = subpackages
    res_df = df.dropna()
    return res_df


print(get_all_attributes(creme))
