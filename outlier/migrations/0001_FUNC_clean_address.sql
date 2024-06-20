create or replace function clean_address(input text) returns text as $$
begin
-- replace punctuation
	input := regexp_replace(input, '#(\d+)', '# \1', 'g');
	input := regexp_replace(input, '[^\w^\d^#]^\m', '', 'g');
	input := regexp_replace(input, '[^\w^\d^#]', ' ', 'g');
	input := regexp_replace(input, 'P.O', 'PO', 'g');
	input := regexp_replace(input, 'P.O.', 'PO', 'g');
	input := regexp_replace(input, 'P O ', 'PO', 'g');
	input := regexp_replace(input, 'P. O.', 'PO', 'g');
	input := regexp_replace(input, '\mSTREET\M', 'ST', 'g');
	input := regexp_replace(input, '\mROAD\M', 'RD', 'g');
	input := regexp_replace(input, '\mAVENUE\M', 'AVE', 'g');
	input := regexp_replace(input, '\mCOURT\M', 'CT', 'g');
	input := regexp_replace(input, '\mFREEWAY\M', 'FWY', 'g');
	input := regexp_replace(input, '\mDRIVE\M', 'DR', 'g');
	input := regexp_replace(input, '\mPARKWAY\M', 'PKWY', 'g'); 
	input := regexp_replace(input, '\mCIRCLE\M', 'CIR', 'g');
	input := regexp_replace(input, '\mLANE\M', 'LN', 'g');
	input := regexp_replace(input, '\mBOULEVARD\M', 'BLVD', 'g');
	input := regexp_replace(input, '\mHIGHWAY\M', 'HWY', 'g');
	input := regexp_replace(input, '\mFLOOR\M', 'FLR', 'g');
	input := regexp_replace(input, '\mSUITE\M', '#', 'g');
	input := regexp_replace(input, '\mSTE\M', '#', 'g');
	input := regexp_replace(input, '\mAPT\M', '#', 'g');
	input := regexp_replace(input, '\mUNIT\M', '#', 'g');
	input := regexp_replace(input, '\mAPARTMENT\M', '#', 'g');
  input := regexp_replace(input, '\s+', ' ', 'g');
  input := regexp_replace(input, '\s(ST|AVE|RD|FWY|CT|DR|PKWY|CIR|BLVD|WAY|HWY|LN)\M', '', 'g');
  input := regexp_replace(input, '(\d+)TH FLR', '# \100000', 'g');
  input := regexp_replace(input, '(\d+) FLR', '# \100000', 'g');
  input := regexp_replace(input, '(\d+)ND FLR', '# \100000', 'g');
  input := regexp_replace(input, '(\d+)RD FLR', '# \100000', 'g');
  input := regexp_replace(input, '(\d+)ST FLR', '# \100000', 'g');
  input := regexp_replace(input, '(# )+', '# ', 'g');
  input := trim(input);
	return input;
end
$$ language plpgsql;

