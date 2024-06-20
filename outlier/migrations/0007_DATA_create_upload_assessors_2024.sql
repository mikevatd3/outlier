
CREATE TABLE assessors_2024 (
	object_id                       BIGINT, 
	parcel_number                   TEXT, 
	ward                            FLOAT(53), 
	address                         TEXT, 
	council_district                FLOAT(53), 
	zip_code                        TEXT, 
	taxpayer_1                      TEXT, 
	taxpayer_2                      TEXT, 
	taxpayer_street                 TEXT, 
	taxpayer_city                   TEXT, 
	taxpayer_state                  TEXT, 
	taxpayer_zip                    TEXT, 
	property_class                  FLOAT(53), 
	property_class_desc             TEXT, 
	property_class_previous         FLOAT(53), 
	use_code                        TEXT, 
	use_code_desc                   TEXT, 
	tax_status                      TEXT, 
	tax_status_description          TEXT, 
	tax_status_previous             TEXT, 
	total_square_footage            FLOAT(53), 
	total_acreage                   FLOAT(53), 
	frontage                        FLOAT(53), 
	depth                           FLOAT(53), 
	homestead_pre                   FLOAT(53), 
	nez                             TEXT, 
	is_improved                     FLOAT(53), 
	num_bldgs                       FLOAT(53), 
	total_floor_area                FLOAT(53), 
	style                           TEXT, 
	year_built                      FLOAT(53), 
	sale_price                      FLOAT(53), 
	sale_date                       TEXT, 
	assessed_value                  FLOAT(53), 
	assessed_value_previous         FLOAT(53), 
	taxable_value                   FLOAT(53), 
	taxable_value_previous          FLOAT(53), 
	economic_condition_factor_neigh TEXT, 
	landmap                         TEXT, 
	related                         TEXT, 
	zoning                          TEXT, 
	historic_designation            TEXT, 
	subdivision                     TEXT, 
	legal_description               TEXT, 
	"Shape__Area"                   FLOAT(53), 
	"Shape__Length"                 FLOAT(53)
);

