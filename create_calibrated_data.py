import tools
import pandas as pd 
import os


def get_xy_soccer(player_num, sport, gps_type='ELITE'):
    dfraw = tools.load_gps_data(gps_type=gps_type, player_num=player_num)
    df = tools.data_gps_clean(dfraw, gps_type=gps_type, player_num=player_num)
    play_time = tools.play_time(sport)
    start = play_time[0]
    end = play_time[1]
    df = tools.cut_df_time(df, start, end)
    if sport == 'soccer': 
        x, y, lat0, lon0 = tools.gps2cart(df['latitude'].values, df['longitude'].values, tools.calib_lat_lon_soccer())
    elif sport == 'basketball': 
        x, y, lat0, lon0 = tools.gps2cart(df['latitude'].values, df['longitude'].values, tools.calib_lat_lon_basketball())
    elif sport == 'volleyball': 
        x, y, lat0, lon0 = tools.gps2cart(df['latitude'].values, df['longitude'].values, tools.calib_lat_lon_volleyball())
    return x, y



def create_data(sport, color):
    print(' ')
    print(f'Creating XY data: {sport} - {color}')
    df = pd.DataFrame()
    for player in tools.get_team_list(sport,color): 
        x, y = get_xy_soccer(player, sport)
        df_trial = pd.DataFrame({f'{player}_x': x, 
                                 f'{player}_y': y})
        df = pd.concat([df, df_trial], axis=1)
        # df[f'{player}_x'] = x
        # df[f'{player}_y'] = y
    folder = f'./data/{sport}/' 
    print(f'File saved in : {folder}')
    os.makedirs(folder,exist_ok=True)
    df.to_csv(f'{folder}/{color}_xy.csv',index=False)



if __name__ == '__main__':
    create_data('soccer', 'blue')
    create_data('soccer', 'orange')
    create_data('basketball', 'blue')
    create_data('basketball', 'orange')
    create_data('volleyball', 'blue')
    create_data('volleyball', 'orange')
    print('Done!')
    print(' ')
