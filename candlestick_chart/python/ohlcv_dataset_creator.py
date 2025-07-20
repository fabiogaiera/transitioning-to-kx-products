# Import necessary libraries
import pykx as kx

"""
CSV format example
datetime,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""


def create_dataframe(csv_file_path, market_open_timespan, market_close_timespan):
    # Upload a CSV file into a kdb+ table
    # P stands for timestamp
    # S stands for symbol
    # F stands for float
    # J stands for long
    trades = kx.q.read.csv(csv_file_path, 'PSFJ')

    trades['date'] = trades['datetime'].date
    trades.set_index('date')

    trades['market_open'] = trades['date'] + kx.TimespanAtom(kx.q(market_open_timespan))
    trades['market_close'] = trades['date'] + kx.TimespanAtom(kx.q(market_close_timespan))

    market_hours_trades = trades.select(

        where=(
                (kx.Column('datetime') >= kx.Column('market_open')) &
                (kx.Column('datetime') <= kx.Column('market_close'))
        )
    )

    aggregated_data = market_hours_trades.select(

        columns={

            'open': kx.Column('price').first(),
            'high': kx.Column('price').max(),
            'low': kx.Column('price').min(),
            'close': kx.Column('price').last(),
            'volume': kx.Column('size').sum(),
        },

        by=kx.Column('date')

    )

    return aggregated_data.pd()
