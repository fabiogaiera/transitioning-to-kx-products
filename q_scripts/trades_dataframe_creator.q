


loadcsvandsavetable: {
    trades: ("PSFJ";enlist ",") 0: `$"/home/fabio/data/IBM_trades.csv"
    trades: select from trades where (`date$timestamp) = 2025.06.06
    trades: select from trades where timestamp within 2025.06.06D13:30:00.000000000 2025.06.06D20:00:00.000000000
    var: select tc: count i by time: 60 xbar timestamp.minute from trades
    show var
 }

loadcsvandsavetable[]