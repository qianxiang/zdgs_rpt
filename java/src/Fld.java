import java.util.List;


/**
 * @author jintian
 * fld_no, khmc, khdz, lxdh, ssds, xqdh, lsh,
            + "zdrq, ckrq, flck, jedx, jehj 
 */
public class Fld implements IReport  {
	public String fld_no;
	public String khmc;
	public String khdz;
	public String lxdh;
	public String ssds;
	public String xqdh;
	public String lsh;
	public String zdrq;
	public String ckrq;
	public String flck;
	public String jedx;
	public String jehj;
	
	private List <FldDetail> fldList;
	
	public List<FldDetail> getList() {
		return fldList;
	}
	public void setFldList(List<FldDetail> fldList) {
		this.fldList = fldList;
	}

	
}
