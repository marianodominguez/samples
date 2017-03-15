require_relative 'coins'

us_dollar = [1, 5, 10, 25, 100]
mx_peso = [1, 2, 5, 10, 20, 50]
weird_currency = [1, 5, 7, 100]

change = ChangeUtil.new

describe ChangeUtil, "#min" do
  it "should give proper change for us dollar" do
    min = change.min(75, us_dollar)
    min.should eq([25,25,25])
  end

  it "should give minimum for weird currency" do
    min = change.min(15, weird_currency);
    min.should eq([1, 7, 7])
  end
end
