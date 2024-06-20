create or replace function clean_taxpayer(input text) returns text as $$
begin
-- replace punctuation
  input := upper(input);
	input := regexp_replace(input, '[^\w^\d^#]^\m', '', 'g');
	input := regexp_replace(input, '[^\w^\d^#]', ' ', 'g');
  input := regexp_replace(input, '\s+', ' ', 'g');
  input := trim(input);
	return input;
end
$$ language plpgsql;

