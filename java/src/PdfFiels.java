import java.io.FileOutputStream;
import java.lang.reflect.Field;
import java.util.List;

import com.itextpdf.text.pdf.AcroFields;
import com.itextpdf.text.pdf.PdfReader;
import com.itextpdf.text.pdf.PdfStamper;

public class PdfFiels {

	static public void manipulatePdf(String src, String dest, IReport report)
			throws Exception {
		PdfReader reader = new PdfReader(src);
		PdfStamper stamper = new PdfStamper(reader, new FileOutputStream(dest));
		reader.close();
		AcroFields form = stamper.getAcroFields();
		copyObjToForm(report, form);
		copyListToForm(report.getList(), form);
		stamper.close();
	}

	// static public void manipulateFldPdf(String src, String dest, Fld fld)
	// throws Exception {

	// BaseFont bfChinese = BaseFont.createFont(
	// "C:\\WINDOWS\\Fonts\\simsun.ttf",
	// BaseFont.IDENTITY_H,BaseFont.NOT_EMBEDDED);
	// Font FontChinese = new Font(bfChinese, 12, Font.NORMAL);

	// }

	static public void copyObjToForm(Object obj, AcroFields form)
			throws Exception {
		for (Field fd : obj.getClass().getDeclaredFields()) {
			if (fd.getName().endsWith("List"))
				continue;
			form.setField(fd.getName(), (String) fd.get(obj));
		}
	}

	static public void copyListToForm(List<?> list, AcroFields form)
			throws Exception {
		int i = 0;
		for (Object obj : list) {

			for (Field fd : obj.getClass().getDeclaredFields()) {
				if (fd.getName().endsWith("List"))
					continue;
				form.setField(fd.getName() + i, (String) fd.get(obj));
			}
			i++;
		}

	}
}
