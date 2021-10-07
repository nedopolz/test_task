import pandas as pd


class ReportFormer:

    def __init__(self, path_to_report: str):
        self.old_df = pd.read_csv(path_to_report, sep=';')
        self.new_df = None

    def init_new_df(self):
        dates = self.old_df['APPLICATION_DT'].unique()
        poses = self.old_df['INTERNAL_ORG_ORIGINAL_RK'].unique()
        poses = list(poses)
        poses.sort()
        data = {
            'Date/Pos': dates
        }
        for pos in poses:
            data.update({str(pos): ''})
            data.update({f'{str(pos)}%': ''})
        self.new_df = pd.DataFrame(data)
        self.new_df = self.new_df.sort_values(by='Date/Pos')
        self.new_df = self.new_df.reset_index(drop=True)
        print(self.new_df)

    def calcualte(self):
        dates = self.new_df['Date/Pos']
        poses = self.old_df['INTERNAL_ORG_ORIGINAL_RK'].unique()
        count = 0
        for date in dates:
            sum_for_day = self.old_df['LOAN_AMOUNT'].where(self.old_df['APPLICATION_DT'] == date)
            sum_for_day_int = sum_for_day.sum()
            for pos in poses:
                sum_of_pos_for_day = sum_for_day.where(self.old_df['INTERNAL_ORG_ORIGINAL_RK'] == pos).sum()

                self.new_df.loc[count, [str(pos), f'{pos}%']] = [sum_of_pos_for_day,
                                                                 (sum_of_pos_for_day / sum_for_day_int)]
            count += 1
        self.new_df.to_csv(path_or_buf=r'data_out.csv')


rf = ReportFormer('data.csv')
rf.init_new_df()
rf.calcualte()
