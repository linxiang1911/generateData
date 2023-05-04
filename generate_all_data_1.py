import pandas as pd
import random
import numpy as np
import os
import logger
def _split_data(df: pd.DataFrame, split_percentage: tuple = (0.8, 0.1)):
    """Method for creating the train, test, validation split of the data.
    
    df : Network dataframe
    split_percentage: Tuple containing the training, testing, and validation ratio respectively. 
    The values of the percentage have to be between 0 and 1.
    """
    
    # Filter interested data for splitting
    treat_relations = df[df['relation'] == 'result']
    
    # Shuffle the dataframe
    treat_relations = treat_relations.sample(frac=1).reset_index(drop=True)
    network = df[df['relation'] != 'result']  # Remaining network data
            
    # Split the data into pre-defined percentage
    train_ratio, val_ratio = split_percentage  # default split is 80/10/10
    train, val, test = np.split(
        treat_relations,
        [
            int(train_ratio * len(treat_relations)),  # train ratio
            int((1 - val_ratio) * len(treat_relations))
        ])        
    
    print(f"Percentages : Train - {round(train.shape[0]/df.shape[0], 2)}\
    Test - {round(test.shape[0]/df.shape[0], 2)} \
    Validate - {round(val.shape[0]/df.shape[0], 2)}"
    )
    
    # Add the original network data to training data
    train = train.append(network, ignore_index=True)   
    print(f"All Train - {round(train.shape[0]/df.shape[0], 2)}")
    return train, test, val
def appendTriple(all_df,str,relation,prob):
    df = pd.read_csv(str, index_col=0)
    # 获取所有列的名称列表
    columns_list = df.columns.tolist()
    # 遍历DataFrame并输出每一列的值
    for column in columns_list:
        for index, row in df.iterrows():
            if row[column]>=prob:
                if column.startswith('etest'):
                    rand_num = random.random()
                    if rand_num>=0.5:
                        new_row = {'source': index, 'relation': relation, 'target':column+':pass'}
                    else:
                        new_row = {'source': index, 'relation': relation, 'target':column+':fail'}
                else: 
                    new_row = {'source': index, 'relation': relation, 'target':column}
                print(new_row)
                all_df = all_df.append(new_row, ignore_index=True)
    return all_df
all_df = pd.DataFrame(columns=['source', 'relation', 'target'])
all_df=appendTriple(all_df,'label_defect.csv','associate',0.004)
all_df=appendTriple(all_df,'label_etest.csv','associate',0.004)
all_df=appendTriple(all_df,'toolIndicatorSPC_defect.csv','associate',0.004)
all_df=appendTriple(all_df,'toolIndicatorSPC_etest.csv','associate',0.004)
all_df=appendTriple(all_df,'toolIndicatorSPC_label.csv','result',0.0153)
all_df.head()
os.makedirs('./data', exist_ok=True)

if not os.path.exists('../data/train.tsv'):
    semicon_train, semicon_test, semicon_val = _split_data(
       all_df
    )
    semicon_train = semicon_train[['source', 'relation', 'target']]
    semicon_test = semicon_test[['source', 'relation', 'target']]
    semicon_val = semicon_val[['source', 'relation', 'target']]
    
    semicon_train.to_csv('./data/train.tsv', sep='\t', index=False, header = False)
    semicon_test.to_csv('./data/test.tsv', sep='\t', index=False, header = False)
    semicon_val.to_csv('./data/val.tsv', sep='\t', index=False, header = False)
else:
    semicon_train = pd.read_csv('./data/train.tsv', sep='\t', names=['source', 'relation', 'target'])
    semicon_test = pd.read_csv('./data/test.tsv', sep='\t', names=['source', 'relation', 'target'])
    semicon_val = pd.read_csv('./data/val.tsv', sep='\t', names=['source', 'relation', 'target'])

semicon_train.head()