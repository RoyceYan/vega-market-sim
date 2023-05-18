from vega_sim.api.market import MarketConfig
from vega_sim.scenario.common.agents import ShapedMarketMaker
from vega_sim.scenario.comprehensive_market.scenario import ComprehensiveMarket
from vega_sim.scenario.curve_market_maker.scenario import CurveMarketMaker
from vega_sim.scenario.ideal_market_maker.scenario import IdealMarketMaker
from vega_sim.scenario.ideal_market_maker_v2.scenario import (
    IdealMarketMaker as IdealMarketMakerV2,
)
from vega_sim.scenario.multi_market.scenario import VegaLoadTest
from vega_sim.scenario.market_crash.scenario import MarketCrash
from vega_sim.scenario.configurable_market.scenario import ConfigurableMarket
from vega_sim.scenario.hedged_market_maker.scenario import HedgedMarket
from vega_sim.scenario.parameter_experiment.scenario import ParameterExperiment
from vega_sim.scenario.fuzzed_markets.scenario import FuzzingScenario


from vega_sim.scenario.common.utils.price_process import (
    get_historic_price_series,
    Granularity,
)

mc = MarketConfig()

CONF = {
    "decimal_places": "1",
    "price_monitoring_parameters": {
        "triggers": [
            {
                "horizon": "60",
                "probability": "0.9999",
                "auction_extension": "5",
            },
            {
                "horizon": "600",
                "probability": "0.9999",
                "auction_extension": "30",
            },
            {
                "horizon": "3600",
                "probability": "0.9999",
                "auction_extension": "120",
            },
            {
                "horizon": "14400",
                "probability": "0.9999",
                "auction_extension": "180",
            },
            {
                "horizon": "43200",
                "probability": "0.9999",
                "auction_extension": "300",
            },
        ]
    },
    "liquidity_monitoring_parameters": {
        "target_stake_parameters": {"time_window": "3600", "scaling_factor": 1},
        "triggering_ratio": "0.7",
        "auction_extension": "1",
    },
    "log_normal": {
        "risk_aversion_parameter": 0.000001,
        "tau": 0.0001140771161,
        "params": {"sigma": 1.5},
    },
    "position_decimal_places": "4",
    "lp_price_range": "0.8",
    "linear_slippage_factor": "0.001",
    "quadratic_slippage_factor": "0.0",
}
for c, v in CONF.items():
    mc.set(c, v)


SCENARIOS = {
    "comprehensive_market": lambda: ComprehensiveMarket(
        market_name="ETH",
        asset_name="USD",
        num_steps=12000,
        market_decimal=2,
        asset_decimal=4,
        market_position_decimal=4,
        initial_price=1000.00,
        spread=10,
        lp_commitamount=500_000,
        initial_asset_mint=10_000_000,
        step_length_seconds=60,
        block_length_seconds=1,
        opening_auction_trade_amount=1,
        market_order_trader_order_intensity=10,
        market_order_trader_order_size=0.01,
        limit_order_trader_quantity=5,
        limit_order_trader_submit_bias=0.1,
        limit_order_trader_cancel_bias=0.1,
        limit_order_trader_order_intensity=10,
        limit_order_trader_order_size=0.1,
        limit_order_trader_mean=-5,
        limit_order_trader_sigma=0.5,
        limit_order_trader_duration=300,
        limit_order_trader_time_in_force_opts={
            "TIME_IN_FORCE_GTC": 0.7,
            "TIME_IN_FORCE_GTT": 0.3,
        },
        num_lp_agents=3,
        num_mo_agents=5,
        num_lo_agents=20,
    ),
    "ideal_market_maker": IdealMarketMaker,
    "ideal_market_maker_v2": lambda: IdealMarketMakerV2(
        num_steps=2000,
        market_decimal=3,
        asset_decimal=5,
        market_position_decimal=2,
        initial_price=1123.11,
        spread=4,
        lp_commitamount=1000000,
        initial_asset_mint=1e8,
        step_length_seconds=60,
        block_length_seconds=1,
        buy_intensity=10,
        sell_intensity=10,
        q_upper=50,
        q_lower=-50,
        kappa=50,
        sigma=5,
        backgroundmarket_tick_spacing=0.002,
        backgroundmarket_number_levels_per_side=25,
        settle_at_end=False,
    ),
    "market_crash": lambda: MarketCrash(
        num_steps=500,
        sigma_pre=1,
        sigma_post=4,
        drift_pre=0.1,
        drift_post=-0.5,
        break_point=200,
        initial_price=100,
        kappa=1.1,
        position_taker_buy_intensity=3,
        position_taker_sell_intensity=0,
        noise_buy_intensity=3,
        noise_sell_intensity=3,
        num_position_traders=5,
        num_noise_traders=20,
        step_length_seconds=60,
        block_length_seconds=1,
        trim_to_min=1,
    ),
    "historic_ideal_market_maker_v2": lambda: IdealMarketMakerV2(
        market_name="ETH",
        asset_name="USD",
        num_steps=290,
        market_decimal=2,
        asset_decimal=4,
        market_position_decimal=4,
        price_process_fn=lambda: get_historic_price_series(
            product_id="ETH-USD", granularity=Granularity.HOUR
        ).values,
        spread=0.01,
        lp_commitamount=250_000,
        initial_asset_mint=10_000_000,
        step_length_seconds=60,
        # step_length_seconds=Granularity.HOUR.value,
        block_length_seconds=1,
        buy_intensity=700_000,
        sell_intensity=700_000,
        q_upper=2,
        q_lower=-2,
        kappa=0.2,
        opening_auction_trade_amount=0.0001,
        backgroundmarket_tick_spacing=0.1,
        backgroundmarket_number_levels_per_side=25,
        market_order_trader_base_order_size=0.01,
    ),
    "historic_shaped_market_maker": lambda: CurveMarketMaker(
        market_name="ETH",
        asset_name="USD",
        num_steps=290,
        market_decimal=2,
        asset_decimal=4,
        market_position_decimal=4,
        price_process_fn=lambda: get_historic_price_series(
            product_id="ETH-USD", granularity=Granularity.HOUR
        ).values,
        lp_commitamount=250_000,
        initial_asset_mint=10_000_000,
        step_length_seconds=60,
        # step_length_seconds=Granularity.HOUR.value,
        block_length_seconds=1,
        q_upper=30,
        q_lower=-30,
        market_maker_curve_kappa=0.2,
        market_maker_assumed_market_kappa=0.2,
        buy_intensity=100,
        sell_intensity=100,
        sensitive_price_taker_half_life=10,
        opening_auction_trade_amount=0.0001,
        market_order_trader_base_order_size=0.01,
    ),
    "shaped_market_maker": lambda: CurveMarketMaker(
        market_name="ETH",
        asset_name="USD",
        num_steps=290,
        market_decimal=2,
        asset_decimal=4,
        market_position_decimal=4,
        initial_price=1000,
        lp_commitamount=250_000,
        initial_asset_mint=10_000_000,
        step_length_seconds=60,
        # step_length_seconds=Granularity.HOUR.value,
        block_length_seconds=1,
        q_upper=30,
        q_lower=-30,
        market_maker_curve_kappa=0.2,
        market_maker_assumed_market_kappa=0.2,
        buy_intensity=100,
        sell_intensity=100,
        sensitive_price_taker_half_life=10,
        opening_auction_trade_amount=0.0001,
        market_order_trader_base_order_size=0.01,
    ),
    "configurable_market": lambda: ConfigurableMarket(
        market_name="RESEARCH: Bitcoin:USD Q3 (Daily)",
        market_code="BTC:USD",
        asset_name="tUSD",
        asset_dp=18,
        num_steps=60 * 24,
        market_config=None,
    ),
    "vega_load_test": lambda: VegaLoadTest(
        num_steps=60 * 24,
        granularity=Granularity.MINUTE,
        step_length_seconds=60,
        block_length_seconds=5,
        transactions_per_block=4000,
        parties_per_market=100,
        orders_per_second=100,
        trades_per_second=1,
    ),
    "hedged_market": lambda: HedgedMarket(
        num_steps=24 * 60,
        step_length_seconds=60,
        block_length_seconds=1,
        price_process_fn=lambda: get_historic_price_series(
            product_id="ETH-USD",
            granularity=Granularity.MINUTE,
            start="2022-06-12 17:00:00",
            end="2022-06-13 17:00:00",
        ).values,
        int_lock=3 * 60 * 60,
        ext_lock=5 * 60,
    ),
    "parameter_experiment": lambda: ParameterExperiment(),
    "fuzz_test": lambda: FuzzingScenario(
        num_steps=2 * 60 * 12,
        step_length_seconds=30,
        block_length_seconds=1,
        transactions_per_block=4096,
    ),
}
