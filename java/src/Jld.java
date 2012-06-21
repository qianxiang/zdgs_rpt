import java.util.List;


public class Jld implements IReport  {
	public String jld_no;
	public String jlyj;
	public String slyj;
	public String jlbh;
	public String slck;
	public String jlrq;
	public String slrq;
	
	private List <JldDetail> jldList;
	public List<JldDetail> getList() {
		return jldList;
	}
	public void setJldList(List<JldDetail> jldList) {
		this.jldList = jldList;
	}

	
}
