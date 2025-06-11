import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime
from geographiclib.geodesic import Geodesic
from matplotlib.patches import Circle, Rectangle, Arc



def load_gps_data(gps_type='PRO', player_num=1):
    try:
        print(f'    -Loading | GPS {gps_type} - Player: {player_num}')
        data_location = f'./rawdata/Kinexon GPS {gps_type}/TUM_TESTING_GPS_{gps_type}_Testing_Player_{player_num}.csv'
        df = pd.read_csv(data_location,sep=';')
        return df
    except Exception as e:
        print(f' !! Error in loading:  GPS {gps_type} - Player: {player_num} !!')
        print(e)
        return pd.DataFrame()



def data_gps_clean(df,gps_type='PRO',player_num=1):
    try:
        print(f'    -Data Clening | GPS {gps_type} - Player: {player_num}')
        df = df.dropna(subset=('longitude in deg')).copy()
        df['time'] = pd.to_datetime(df['formatted local time'], format="%d/%m/%Y, %I:%M:%S.%f %p")
        df['time'] = df['time'].dt.time
        df.columns
        df_interest = df[['time','latitude in deg','longitude in deg']].rename(columns={'latitude in deg':'latitude',
                                                                                        'longitude in deg':'longitude'}).reset_index(drop=True)
        return df_interest
    except Exception as e:
        print(f' !! Error in data cleaning:  GPS {gps_type} - Player: {player_num} !!')
        print(e)
        return pd.DataFrame()



def get_team_list(sport, color): 
    if sport == 'soccer': 
        if color == 'blue': 
            team_list = [ 9, 10, 11]
        elif color == 'orange': 
            team_list = [6, 5, 13]
        elif color == 'ref': 
            team_list = [12]
    
    elif sport == 'basketball':
        if color == 'blue': 
            team_list = [6, 9, 12, 8]
        elif color == 'orange': 
            team_list = [7, 10, 5, 4]
        else: 
            team_list = []

    elif sport == 'volleyball':
        if color == 'blue': 
            team_list = [5, 10, 3, 4]
        elif color == 'orange': 
            team_list = [12, 9, 6, 8]
        else: 
            team_list = []

    return team_list



def gps2cart(lat, lon, mcampo):
    """
    Converte coordenadas GPS (lat, lon) para sistema cartesiano local,
    baseado em pontos de calibração definidos em mcampo.

    Parâmetros:
        lat: vetor de latitudes (em graus)
        lon: vetor de longitudes (em graus)
        mcampo: array (4x2), pontos GPS: origem, base_x, base_y, etc.

    Retorna:
        x_coord_nova, y_coord_nova: coordenadas transformadas
        lat_origin, lon_origin: origem usada para a transformação
    """
    # Origem
    lat_origin = mcampo[0, 0]
    lon_origin = mcampo[0, 1]

    # Vetores de saída
    x_coord = []
    y_coord = []

    # Para cada ponto, calcular distância e azimute
    for la, lo in zip(lat, lon):
        g = Geodesic.WGS84.Inverse(lat_origin, lon_origin, la, lo)
        dist = g['s12']
        az = g['azi1']
        x = dist * np.sin(np.radians(az))
        y = dist * np.cos(np.radians(az))
        x_coord.append(x)
        y_coord.append(y)

    # Calibrar base X e Y
    x_base = []
    y_base = []
    for i in range(1, 3):  # ponto 1 e 2 de mcampo: base_x e base_y
        lat_i, lon_i = mcampo[i]
        g = Geodesic.WGS84.Inverse(lat_origin, lon_origin, lat_i, lon_i)
        dist = g['s12']
        az = g['azi1']
        x_i = dist * np.sin(np.radians(az))
        y_i = dist * np.cos(np.radians(az))
        x_base.append(x_i)
        y_base.append(y_i)

    # Vetores normalizados
    v1 = np.array([x_base[0], y_base[0]])
    v2 = np.array([x_base[1], y_base[1]])
    v1_norm = v1 / np.linalg.norm(v1)
    v2_norm = v2 / np.linalg.norm(v2)

    # Matriz de rotação base
    B = np.column_stack((v1_norm, v2_norm))  # 2x2

    # Aplicar transformação para cada ponto
    coords = np.vstack((x_coord, y_coord))  # 2xN
    transformed = B.T @ coords              # 2xN

    x_coord_nova = transformed[0, :].tolist()
    y_coord_nova = transformed[1, :].tolist()

    return x_coord_nova, y_coord_nova, lat_origin, lon_origin



def calib_lat_lon_soccer():
    p1 = [48.181346413098815, 11.544539229252987]
    p2 = [48.18108968820917, 11.544539260391772]
    p3 = [48.18134831145872, 11.544804090533203]
    p4 = [48.18107728200126, 11.544539640862254]
    pontos = [p1, p2, p3, p4]
    df_coords = np.array(pd.DataFrame(pontos, columns=['latitude', 'longitude']))
    return df_coords



def calib_lat_lon_basketball():
    p1 = [48.18143019726294, 11.543401703232329]
    p2 = [48.18119805612524, 11.543403810255011]
    p3 = [48.18143108648108, 11.5436039828416]
    p4 = [48.18119851729151, 11.543607638167833]
    pontos = [p1, p2, p3, p4]
    df_coords = np.array(pd.DataFrame(pontos, columns=['latitude', 'longitude']))
    return df_coords



def calib_lat_lon_volleyball():
    p1 = [48.181155230274534, 11.544923876379421]
    p2 = [48.18101258122396, 11.544920397963018]
    p3 = [48.18115292991193, 11.545032204945553]
    p4 = [48.1810084677825, 11.545030824767817]
    pontos = [p1, p2, p3, p4]
    df_coords = np.array(pd.DataFrame(pontos, columns=['latitude', 'longitude']))
    return df_coords



def calib_soccer_real():
    p1 = [0, 0]
    p2 = [30, 0]
    p3 = [0, 20]
    p4 = [30,20]
    pontos = [p1, p2, p3, p4]
    df_coords = pd.DataFrame(pontos, columns=['latitude', 'longitude'])
    return df_coords



def play_time(sport): 
    if sport =='soccer': 
        time = ['11:38:30', '11:48:30']
    elif sport == 'basketball': 
        time = ['12:01:05', '12:10:45']
    elif sport == 'volleyball':
        time = ['12:17:45', '12:27:45']
    else:
        time = []
    return time



def cut_df_time(df, str_start_time=None, str_end_time=None):
    try:
        if str_start_time is None:
            str_start_time = str(df['time'].iloc[0]).split('.')[0]
        if str_end_time is None:
            str_end_time = str(df['time'].iloc[-1]).split('.')[0]
        start_time = datetime.strptime(str_start_time, '%H:%M:%S').time()
        end_time = datetime.strptime(str_end_time, '%H:%M:%S').time()
        df_filtered = df[(df['time'] >= start_time) & (df['time'] <= end_time)]
        return df_filtered
    except Exception as e:
        print(f' !! Error in trim data by time: Start: {str_start_time} - End: {str_end_time}!!')
        print(e)
        return pd.DataFrame()



def draw_soccer_field(tam=[30, 20]):
    comp, larg = tam
    c = (0, 0.7, 0)  # cor de fundo

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor(c)
    ax.set_xlim(-2, comp + 2)
    ax.set_ylim(-2, larg + 2)
    ax.set_aspect('equal')
    
    # Linha central
    ax.plot([comp / 2, comp / 2], [0, larg], 'w-', linewidth=2.5)

    # Linhas de fundo e laterais
    ax.plot([0, 0], [0, larg], 'w-', linewidth=2.5)
    ax.plot([comp, comp], [0, larg], 'w-', linewidth=2.5)
    ax.plot([0, comp], [0, 0], 'w-', linewidth=2.5)
    ax.plot([0, comp], [larg, larg], 'w-', linewidth=2.5)

    # Círculo central
    ang = np.linspace(-np.pi, np.pi, 100)
    x_circ = 3 * np.cos(ang) + comp / 2
    y_circ = 3 * np.sin(ang) + larg / 2
    ax.plot(x_circ, y_circ, 'w', linewidth=2.5)

    # Áreas grandes - esquerda
    ax.plot([comp * 0.16, comp * 0.16], [(larg / 2) - comp * 0.16, (larg / 2) + comp * 0.16], 'w', linewidth=2.5)
    ax.plot([0, comp * 0.16], [(larg / 2) - comp * 0.16, (larg / 2) - comp * 0.16], 'w', linewidth=2.5)
    ax.plot([0, comp * 0.16], [(larg / 2) + comp * 0.16, (larg / 2) + comp * 0.16], 'w', linewidth=2.5)

    # Áreas pequenas - esquerda
    ax.plot([comp * 0.07, comp * 0.07], [(larg / 2) - comp * 0.07, (larg / 2) + comp * 0.07], 'w', linewidth=2.5)
    ax.plot([0, comp * 0.07], [(larg / 2) - comp * 0.07, (larg / 2) - comp * 0.07], 'w', linewidth=2.5)
    ax.plot([0, comp * 0.07], [(larg / 2) + comp * 0.07, (larg / 2) + comp * 0.07], 'w', linewidth=2.5)

    # Áreas grandes - direita
    ax.plot([comp * 0.84, comp * 0.84], [(larg / 2) - comp * 0.16, (larg / 2) + comp * 0.16], 'w', linewidth=2.5)
    ax.plot([comp - comp * 0.16, comp], [(larg / 2) - comp * 0.16, (larg / 2) - comp * 0.16], 'w', linewidth=2.5)
    ax.plot([comp - comp * 0.16, comp], [(larg / 2) + comp * 0.16, (larg / 2) + comp * 0.16], 'w', linewidth=2.5)

    # Áreas pequenas - direita
    ax.plot([comp * 0.93, comp * 0.93], [(larg / 2) - comp * 0.07, (larg / 2) + comp * 0.07], 'w', linewidth=2.5)
    ax.plot([comp - comp * 0.07, comp], [(larg / 2) - comp * 0.07, (larg / 2) - comp * 0.07], 'w', linewidth=2.5)
    ax.plot([comp - comp * 0.07, comp], [(larg / 2) + comp * 0.07, (larg / 2) + comp * 0.07], 'w', linewidth=2.5)

    # Pontos de pênalti e centro
    ax.plot(comp * 0.1, larg / 2, 'w.', markersize=15)
    ax.plot(comp * 0.9, larg / 2, 'w.', markersize=15)
    ax.plot(comp / 2, larg / 2, 'w.', markersize=15)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines[:].set_visible(False)
    return fig, ax 




def draw_basketball_court(ax=None, linecolor='white', lw=1.5, courtcolor='#CC5500', remove_axis=False, court_width= 15.05, court_length=28.4):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 5))

    hoop_distance = 1.2
    paint_length = 5.8
    paint_width_outer = 4.9
    paint_width_inner = 3.6
    restricted_diameter = 2.6
    three_point_radius = 6.75
    center_circle_radius = 1.8

    def draw_half_court(origin_x, invert=False):
        direction = -1 if invert else 1
        elems = []

        # Cesta e tabela
        hoop = Circle((origin_x + direction * hoop_distance, court_width / 2), 0.2, linewidth=lw, color=linecolor, fill=False)
        backboard = Rectangle((origin_x + direction * (hoop_distance - 0.1), court_width / 2 - 1), 0.1, 2, linewidth=lw, color=linecolor)

        # Garrafão
        outer_box = Rectangle((origin_x, court_width / 2 - paint_width_outer / 2), direction * paint_length, paint_width_outer, linewidth=lw, color=linecolor, fill=False)
        inner_box = Rectangle((origin_x, court_width / 2 - paint_width_inner / 2), direction * paint_length, paint_width_inner, linewidth=lw, color=linecolor, fill=False)

        # Arcos do lance livre
        top_ft_arc = Arc((origin_x + direction * paint_length, court_width / 2), paint_width_inner, paint_width_inner,
                         theta1=270 if not invert else 90, theta2=90 if not invert else 270, linewidth=lw, color=linecolor)
        bottom_ft_arc = Arc((origin_x + direction * paint_length, court_width / 2), paint_width_inner, paint_width_inner,
                            theta1=90 if not invert else 270, theta2=270 if not invert else 90, linewidth=lw, color=linecolor, linestyle='dashed')

        # Área restrita
        restricted = Arc((origin_x + direction * hoop_distance, court_width / 2), restricted_diameter, restricted_diameter,
                         theta1=270 if not invert else 90, theta2=90 if not invert else 270, linewidth=lw, color=linecolor)

        # Arco de 3 pontos
        three_arc = Arc((origin_x + direction * (hoop_distance + 1), court_width / 2), 13.5, 13.5,
                        theta1=270 if not invert else 90, theta2=90 if not invert else 270, linewidth=lw, color=linecolor)

        # Linhas de 3 pontos dos cantos
        corner_three_a = Rectangle((origin_x, 0.77), direction * 2.6, 0, linewidth=lw, color=linecolor)
        corner_three_b = Rectangle((origin_x, court_width - 0.77), direction * 2.6, 0, linewidth=lw, color=linecolor)

        elems += [hoop, backboard, outer_box, inner_box, top_ft_arc, bottom_ft_arc,
                  restricted, three_arc, corner_three_a, corner_three_b]
        return elems

    # Lado esquerdo (0) e lado direito (quadra invertida a partir da borda final)
    left_half = draw_half_court(0, invert=False)
    right_half = draw_half_court(court_length, invert=True)

    # Círculo central
    center_circle = Circle((court_length / 2, court_width / 2), center_circle_radius, linewidth=lw, color=linecolor, fill=False)

    # Linhas externas
    outer_lines = Rectangle((0, 0), court_length, court_width, linewidth=lw, color=linecolor, fill=False)

    for el in left_half + right_half + [center_circle, outer_lines]:
        ax.add_patch(el)

    ax.set_xlim(-1, court_length + 1)
    ax.set_ylim(-1, court_width + 1)
    ax.set_aspect('equal')
    ax.set_facecolor(courtcolor)

    if remove_axis:
        ax.set_xticks([])
        ax.set_yticks([])

    return fig, ax

