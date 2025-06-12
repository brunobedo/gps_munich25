import calculate_stretchindex
import calculate_width_length
import calculate_team_area
import calculate_teamspread
import argparse


def calculate_all_variables(sport, save=True):
    print(f'Calculating all variables for {sport.capitalize()}...')
    # Calculate area
    df_b_area, df_o_area, anim_area = calculate_team_area.calculate_area(sport, save=save)
    print(' ')
    # Calculate stretch index
    df_b_stretch, df_o_stretch, anim_stretch = calculate_stretchindex.calculate_stretchindex(sport, save=save)
    print(' ')
    # Calculate team spread
    df_b_spread, df_o_spread, anim_spread = calculate_teamspread.calculate_teamspread(sport, save=save)
    print(' ')
    # Calculate width and length
    df_b_width_length, df_o_width_length, anim_width_length = calculate_width_length.calculate_width_length(sport, save=save)

    return {
        'area': (df_b_area, df_o_area, anim_area),
        'stretch_index': (df_b_stretch, df_o_stretch, anim_stretch),
        'team_spread': (df_b_spread, df_o_spread, anim_spread),
        'width_length': (df_b_width_length, df_o_width_length, anim_width_length)
    }
if __name__ == '__main__':
    print('-------------------------------------------------')
    print('Starting calculations of all variables...')
    print(' ')
    parser = argparse.ArgumentParser(description='Calculate all variables for a specific sport.')
    parser.add_argument(
        '--sport',
        type=str,
        default='soccer',
        choices=['basketball', 'soccer', 'volleyball'],
        help='Sport to calculate variables for (default: soccer)'
    )

    args = parser.parse_args()
    sport = args.sport.lower()

    results = calculate_all_variables(sport, save=True)
    
    print(f'Calculations completed for {sport.capitalize()}!')
    print(' ')